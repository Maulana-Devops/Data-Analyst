from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.formatting import format_int, format_percent, format_rupiah
from src.metrics import kpi_summary, missing_months, missing_quantity_count, monthly_revenue_trend


def _rupiah_ticks(vmax: float):
    if vmax is None or vmax <= 0:
        return None, None
    steps = 4
    vals = [vmax * i / steps for i in range(steps + 1)]
    return vals, [format_rupiah(v) for v in vals]


def _trend_figure(trend: pd.DataFrame, missing: list[str]) -> go.Figure:
    hover = [
        format_rupiah(value) if pd.notna(value) else "Tidak ada transaksi (bukan Rp0)"
        for value in trend["Revenue"]
    ]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=trend["Periode"],
            y=trend["Revenue"],
            mode="lines+markers",
            name="Revenue",
            connectgaps=False,
            text=hover,
            hovertemplate="%{x}<br>Revenue: %{text}<extra></extra>",
        )
    )

    for month in missing[:6]:
        fig.add_annotation(
            x=month,
            y=1.0,
            xref="x",
            yref="paper",
            yanchor="bottom",
            yshift=2,
            text="tanpa transaksi",
            showarrow=False,
            font=dict(color="#b00020", size=10),
        )

    tickvals, ticktext = _rupiah_ticks(trend["Revenue"].max(skipna=True))
    fig.update_yaxes(tickvals=tickvals, ticktext=ticktext)
    fig.update_layout(
        height=420,
        margin=dict(l=10, r=10, t=40, b=10),
        yaxis_title="Revenue",
        hovermode="x unified",
    )
    return fig


def _render_kpis(df: pd.DataFrame) -> None:
    kpi = kpi_summary(df)
    row1 = st.columns(4)
    row1[0].metric("Revenue", format_rupiah(kpi["revenue"]))
    row1[1].metric("Orders", format_int(kpi["orders"]))
    row1[2].metric("Total Unit Tercatat", format_int(kpi["total_unit_tercatat"]))
    row1[3].metric("AOV", format_rupiah(kpi["aov"], 2))

    row2 = st.columns(4)
    row2[0].metric("Cancellation Rate", format_percent(kpi["cancellation_rate"]))
    row2[1].metric("Order Return Rate", format_percent(kpi["order_return_rate"]))
    row2[2].metric("Returned Orders", format_int(kpi["returned_orders"]))
    row2[3].metric("Returned Quantity", format_int(kpi["returned_quantity"]))


def render(df: pd.DataFrame, full_df: pd.DataFrame, start=None, end=None) -> None:
    st.header("Executive Overview")

    if df.empty:
        st.warning("Tidak ada data pada filter saat ini.")
        _render_definitions(full_df, [])
        return

    _render_kpis(df)

    st.subheader("Tren Revenue Bulanan")
    trend = monthly_revenue_trend(df, start=start, end=end)
    if trend.empty:
        st.info("Tren tidak dapat dihitung pada filter saat ini.")
    else:
        current_missing = trend.loc[~trend["Has_Transactions"], "Periode"].tolist()
        st.plotly_chart(
            _trend_figure(trend, current_missing),
            use_container_width=True,
        )
        if current_missing:
            st.caption(
                "Bulan tanpa transaksi pada cakupan saat ini (ditampilkan sebagai "
                "celah, bukan revenue Rp0): " + ", ".join(current_missing) + "."
            )
        else:
            st.caption("Tidak ada bulan kosong pada cakupan filter saat ini.")

    st.divider()
    _render_definitions(df, missing_months(full_df))


def _render_definitions(df: pd.DataFrame, dataset_missing: list[str]) -> None:
    with st.expander("Definisi KPI & catatan data", expanded=False):
        st.markdown(
            "- **Revenue** = jumlah `Total Pembayaran` pada order terfilter.\n"
            "- **Orders** = jumlah `order_id` unik pada order terfilter.\n"
            "- **Total Unit Tercatat** = jumlah `total_qty`; nilai kosong "
            "dikecualikan secara alami oleh agregasi dan **tidak diimputasi**.\n"
            "- **AOV** = Revenue dibagi **seluruh Orders**, termasuk order batal "
            "(order batal bernilai Rp0).\n"
            "- **Cancellation Rate** = Cancelled Orders ÷ seluruh Orders.\n"
            "- **Order Return Rate** = Returned Orders ÷ seluruh Orders "
            "(berbasis order). *Quantity Return Rate tidak ditampilkan karena "
            "denominatornya belum diputuskan.*\n"
            "- **Returned Quantity** = jumlah `total_returned_qty`.\n"
            "- Rate disimpan sebagai desimal 0–1 dan diformat sebagai "
            "persentase hanya pada tampilan.\n"
            "- **Profit, jumlah pelanggan, dan Discount Rate tidak ditampilkan** "
            "karena field/denominator yang sesuai tidak tersedia atau belum "
            "diputuskan."
        )

        missing_qty = missing_quantity_count(df)
        st.markdown(
            f"- **Missing `total_qty`** pada cakupan filter ini: "
            f"**{format_int(missing_qty)}** order (tetap kosong, tidak diimputasi)."
        )

        if dataset_missing:
            st.markdown(
                "- **Bulan tanpa transaksi pada dataset penuh** (bukan revenue "
                "Rp0): " + ", ".join(dataset_missing) + "."
            )
        else:
            st.markdown("- Tidak ada bulan tanpa transaksi pada dataset penuh.")
