from __future__ import annotations

import pandas as pd
import streamlit as st

from src.charts import NEUTRAL_COLOR, SECONDARY_COLOR, bar_chart, empty_figure
from src.formatting import format_int, format_percent, format_rupiah
from src.metrics import (
    CATEGORY_COLUMN,
    PROVINCE_COLUMN,
    cancellation_reason_summary,
    cancelled_orders,
    orders,
    returns_summary,
    returned_orders,
    returned_quantity,
    status_summary,
)

TOP_REASONS = 10


def _status_figure(status: pd.DataFrame):
    ordered = status.sort_values("Orders", ascending=False)
    return bar_chart(
        ordered["Status"],
        ordered["Orders"],
        title="Distribusi Order menurut Status_Analisis",
        category_title="Status_Analisis",
        value_title="Jumlah order",
        value_formatter=format_int,
        color=NEUTRAL_COLOR,
        height=380,
    )


def _cancellation_figure(reasons: pd.DataFrame, top_n: int):
    top = reasons.head(top_n).sort_values("Orders", ascending=True)
    if top.empty:
        return empty_figure("Tidak ada order batal pada cakupan filter ini.")
    return bar_chart(
        top["Alasan"],
        top["Orders"],
        title=f"Top {top_n} Alasan Pembatalan (berdasarkan jumlah order batal)",
        category_title="Alasan pembatalan",
        value_title="Jumlah order batal",
        value_formatter=format_int,
        orientation="h",
        color=SECONDARY_COLOR,
        height=max(360, 32 * len(top) + 120),
    )


def _returns_figure(returns: pd.DataFrame, label_column: str, top_n: int):
    top = returns.head(top_n)
    top = top[top["ReturnedOrders"] > 0].sort_values("ReturnedOrders", ascending=True)
    if top.empty:
        return empty_figure("Tidak ada order retur pada cakupan filter ini.")
    return bar_chart(
        top[label_column],
        top["ReturnedOrders"],
        title=f"Top {top_n} {label_column} — jumlah order retur",
        category_title=label_column,
        value_title="Jumlah order retur (order_id unik)",
        value_formatter=format_int,
        orientation="h",
        color=SECONDARY_COLOR,
        height=max(340, 30 * len(top) + 120),
    )


def _status_table(status: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Status_Analisis": status["Status"],
            "Orders": status["Orders"].map(format_int),
            "Share of Orders": status["Share"].map(format_percent),
            "Revenue": status["Revenue"].map(format_rupiah),
        }
    )


def _returns_table(returns: pd.DataFrame, label_column: str, top_n: int) -> pd.DataFrame:
    top = returns.head(top_n)
    return pd.DataFrame(
        {
            label_column: top[label_column],
            "Order Retur": top["ReturnedOrders"].map(format_int),
            "Unit Retur": top["ReturnedQuantity"].map(format_int),
            "Total Order": top["TotalOrders"].map(format_int),
            "Order Return Rate": top["OrderReturnRate"].map(format_percent),
        }
    )


def render(df: pd.DataFrame, full_df: pd.DataFrame, start=None, end=None) -> None:
    st.header("Order Operations")

    if df.empty:
        st.warning("Tidak ada data pada filter saat ini.")
        st.plotly_chart(empty_figure(), use_container_width=True)
        return

    status = status_summary(df)
    reasons = cancellation_reason_summary(df)
    total_orders = orders(df)

    row = st.columns(4)
    row[0].metric("Total Orders", format_int(total_orders))
    row[1].metric("Order Batal", format_int(cancelled_orders(df)))
    row[2].metric("Order Retur", format_int(returned_orders(df)))
    row[3].metric("Unit Retur", format_int(returned_quantity(df)))

    st.subheader("Distribusi Status")
    st.caption(
        "Menggunakan `Status_Analisis`. **Share of Orders** = Orders status ÷ "
        "seluruh Orders pada cakupan filter (setiap order dihitung tepat sekali)."
    )
    st.plotly_chart(_status_figure(status), use_container_width=True)
    st.dataframe(_status_table(status), use_container_width=True, hide_index=True)

    st.subheader("Alasan Pembatalan")
    cancelled_total = int(reasons["Orders"].sum()) if not reasons.empty else 0
    st.caption(
        "Hanya mencakup order dengan `Is_Cancelled = True` (alasan untuk order "
        f"non-batal bernilai 'Tidak dibatalkan' dan dikeluarkan). Denominator = "
        f"{format_int(cancelled_total)} order batal pada cakupan ini; tiap order "
        "batal dihitung sekali."
    )
    st.plotly_chart(_cancellation_figure(reasons, TOP_REASONS), use_container_width=True)
    if not reasons.empty:
        reason_table = pd.DataFrame(
            {
                "Alasan Pembatalan": reasons["Alasan"],
                "Order Batal": reasons["Orders"].map(format_int),
            }
        )
        st.dataframe(reason_table, use_container_width=True, hide_index=True)
        with st.expander("Semua alasan pembatalan"):
            st.dataframe(reason_table, use_container_width=True, hide_index=True)

    st.subheader("Retur per Kategori dan Provinsi")
    st.caption(
        "**Order Retur** (unit = order, `order_id` unik) berbeda dari **Unit Retur** "
        "(unit = item, `total_returned_qty`); keduanya tidak dicampur. "
        "**Order Return Rate** memakai definisi berbasis order yang sama "
        "(order retur ÷ total order grup). *Quantity Return Rate tidak ditampilkan "
        "karena denominatornya belum diputuskan.*"
    )

    category_returns = returns_summary(df, CATEGORY_COLUMN)
    province_returns = returns_summary(df, PROVINCE_COLUMN)

    st.markdown("**Kategori dengan order retur terbanyak**")
    st.plotly_chart(
        _returns_figure(category_returns, CATEGORY_COLUMN, 10), use_container_width=True
    )
    st.dataframe(
        _returns_table(category_returns, CATEGORY_COLUMN, 10),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("**Provinsi dengan order retur terbanyak**")
    st.plotly_chart(
        _returns_figure(province_returns, PROVINCE_COLUMN, 10), use_container_width=True
    )
    st.dataframe(
        _returns_table(province_returns, PROVINCE_COLUMN, 10),
        use_container_width=True,
        hide_index=True,
    )
