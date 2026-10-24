from __future__ import annotations

import pandas as pd
import streamlit as st

from src.charts import NEUTRAL_COLOR, PRIMARY_COLOR, bar_chart, empty_figure
from src.formatting import format_int, format_percent, format_rupiah
from src.metrics import (
    SHIPPING_METHOD_COLUMN,
    missing_months,
    missing_quantity_count,
    missing_value_summary,
    orders,
    revenue,
    shipping_method_summary,
    shipping_summary,
)

TOP_SHIPPING = 10


def _shipping_comparison_figure(summary: dict, total_revenue: float):
    labels = [
        "Revenue",
        "Perkiraan Ongkos Kirim",
        "Estimasi Potongan Biaya Pengiriman",
        "Ongkos Kirim Dibayar oleh Pembeli",
    ]
    values = [
        total_revenue,
        summary["cost_estimate"]["total"],
        summary["subsidy_estimate"]["total"],
        summary["paid_by_buyer"]["total"],
    ]
    return bar_chart(
        labels,
        values,
        title="Perbandingan Nilai Transaksi dan Komponen Ongkir (nilai agregat)",
        category_title="Komponen",
        value_title="Nilai agregat",
        value_formatter=format_rupiah,
        color=PRIMARY_COLOR,
        height=420,
    )


def _shipping_method_figure(methods: pd.DataFrame, top_n: int):
    top = methods.head(top_n).sort_values("Orders", ascending=True)
    if top.empty:
        return empty_figure("Tidak ada data opsi pengiriman pada cakupan ini.")
    return bar_chart(
        top[SHIPPING_METHOD_COLUMN],
        top["Orders"],
        title=f"Top {top_n} Opsi Pengiriman (berdasarkan jumlah order)",
        category_title="Opsi pengiriman",
        value_title="Jumlah order",
        value_formatter=format_int,
        orientation="h",
        color=NEUTRAL_COLOR,
        height=max(360, 30 * len(top) + 120),
    )


def render(df: pd.DataFrame, full_df: pd.DataFrame, start=None, end=None) -> None:
    st.header("Shipping & Data Quality")

    if df.empty:
        st.warning("Tidak ada data pada filter saat ini.")
        st.plotly_chart(empty_figure(), use_container_width=True)
        return

    shipping = shipping_summary(df)
    total_revenue = revenue(df)

    row = st.columns(4)
    row[0].metric("Perkiraan Ongkos Kirim", format_rupiah(shipping["cost_estimate"]["total"]))
    row[1].metric(
        "Ongkir Dibayar Pembeli", format_rupiah(shipping["paid_by_buyer"]["total"])
    )
    row[2].metric(
        "Estimasi Potongan Ongkir", format_rupiah(shipping["subsidy_estimate"]["total"])
    )
    row[3].metric("Missing total_qty", format_int(missing_quantity_count(df)))

    st.subheader("Ringkasan Ongkir")
    st.caption(
        "Nilai ditampilkan apa adanya dari kolom sumber. Skema dataset tidak "
        "membuktikan siapa yang menanggung tiap komponen ongkir, sehingga tidak "
        "disimpulkan siapa pembayarnya dan tidak ada klaim margin/profit."
    )
    st.plotly_chart(
        _shipping_comparison_figure(shipping, total_revenue), use_container_width=True
    )

    shipping_table = pd.DataFrame(
        {
            "Kolom": [
                "Perkiraan Ongkos Kirim",
                "Ongkos Kirim Dibayar oleh Pembeli",
                "Estimasi Potongan Biaya Pengiriman",
            ],
            "Total": [
                format_rupiah(shipping["cost_estimate"]["total"]),
                format_rupiah(shipping["paid_by_buyer"]["total"]),
                format_rupiah(shipping["subsidy_estimate"]["total"]),
            ],
            "Order > 0": [
                format_int(shipping["cost_estimate"]["orders_positive"]),
                format_int(shipping["paid_by_buyer"]["orders_positive"]),
                format_int(shipping["subsidy_estimate"]["orders_positive"]),
            ],
            "Nilai Kosong": [
                format_int(shipping["cost_estimate"]["missing"]),
                format_int(shipping["paid_by_buyer"]["missing"]),
                format_int(shipping["subsidy_estimate"]["missing"]),
            ],
        }
    )
    st.dataframe(shipping_table, use_container_width=True, hide_index=True)

    st.subheader("Opsi Pengiriman")
    methods = shipping_method_summary(df)
    st.caption(
        "Diurutkan berdasarkan **jumlah order** menurun. Revenue dihitung dari "
        "`Total Pembayaran` dan Orders dari `order_id` unik."
    )
    st.plotly_chart(_shipping_method_figure(methods, TOP_SHIPPING), use_container_width=True)
    method_table = pd.DataFrame(
        {
            "Opsi Pengiriman": methods.head(TOP_SHIPPING)[SHIPPING_METHOD_COLUMN],
            "Orders": methods.head(TOP_SHIPPING)["Orders"].map(format_int),
            "Revenue": methods.head(TOP_SHIPPING)["Revenue"].map(format_rupiah),
        }
    )
    st.dataframe(method_table, use_container_width=True, hide_index=True)

    st.subheader("Profil Kualitas Data")
    missing_qty = missing_quantity_count(df)
    st.markdown(
        f"- **Missing `total_qty`** pada cakupan filter: **{format_int(missing_qty)}** "
        "order. Nilai kosong tetap kosong dan tidak diimputasi."
    )

    missing_table = missing_value_summary(df)
    if missing_table.empty:
        st.markdown("- Tidak ada kolom dengan nilai kosong pada cakupan filter ini.")
    else:
        st.markdown("- Kolom dengan nilai kosong pada cakupan filter:")
        display = pd.DataFrame(
            {
                "Kolom": missing_table["Kolom"],
                "Jumlah Missing": missing_table["Jumlah Missing"].map(format_int),
                "Persentase": missing_table["Persentase"].map(format_percent),
            }
        )
        st.dataframe(display, use_container_width=True, hide_index=True)

    dataset_missing = missing_months(full_df)
    if dataset_missing:
        st.markdown(
            "- **Bulan tanpa transaksi pada kalender dataset penuh** (bukan revenue "
            "Rp0): " + ", ".join(dataset_missing) + "."
        )
    else:
        st.markdown("- Tidak ada bulan tanpa transaksi pada kalender dataset penuh.")

    zero_revenue_orders = int((df["Total Pembayaran"] == 0).sum())
    st.markdown(
        f"- Order dengan `Total Pembayaran` = Rp0 pada cakupan filter: "
        f"**{format_int(zero_revenue_orders)}** (berasal dari data; tidak "
        "diasumsikan sama dengan order batal)."
    )
    st.caption(
        "Dataset ini sintetis. Ringkasan kualitas data bersifat deskriptif dan "
        "tidak menyimpulkan performa atau profitabilitas."
    )
