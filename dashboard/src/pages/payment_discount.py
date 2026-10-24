from __future__ import annotations

import pandas as pd
import streamlit as st

from src.charts import PRIMARY_COLOR, SECONDARY_COLOR, bar_chart, empty_figure
from src.formatting import format_int, format_rupiah
from src.metrics import (
    PAYMENT_COLUMN,
    discount_summary,
    orders,
    payment_summary,
    revenue,
)


def _payment_revenue_figure(payment: pd.DataFrame):
    top = payment.sort_values("Revenue", ascending=True)
    return bar_chart(
        top[PAYMENT_COLUMN],
        top["Revenue"],
        title="Revenue per Metode Pembayaran",
        category_title="Metode pembayaran",
        value_title="Revenue",
        value_formatter=format_rupiah,
        orientation="h",
        height=max(380, 30 * len(top) + 120),
    )


def _payment_discount_figure(payment: pd.DataFrame):
    top = payment[payment["Discount"] > 0].sort_values("Discount", ascending=True)
    if top.empty:
        return empty_figure("Tidak ada diskon (> 0) pada cakupan filter ini.")
    return bar_chart(
        top[PAYMENT_COLUMN],
        top["Discount"],
        title="Total Diskon per Metode Pembayaran (hanya nilai > 0)",
        category_title="Metode pembayaran",
        value_title="Total Diskon",
        value_formatter=format_rupiah,
        orientation="h",
        color=SECONDARY_COLOR,
        height=max(320, 30 * len(top) + 120),
    )


def _payment_table(payment: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            PAYMENT_COLUMN: payment[PAYMENT_COLUMN],
            "Revenue": payment["Revenue"].map(format_rupiah),
            "Orders": payment["Orders"].map(format_int),
            "Quantity": payment["Quantity"].map(format_int),
            "AOV": payment["AOV"].map(lambda value: format_rupiah(value, 2)),
            "Total Diskon": payment["Discount"].map(format_rupiah),
        }
    )


def render(df: pd.DataFrame, full_df: pd.DataFrame, start=None, end=None) -> None:
    st.header("Payment & Discount")

    if df.empty:
        st.warning("Tidak ada data pada filter saat ini.")
        st.plotly_chart(empty_figure(), use_container_width=True)
        return

    payment = payment_summary(df)
    discount = discount_summary(df)

    zero_revenue_methods = payment.loc[payment["Revenue"] == 0, PAYMENT_COLUMN].tolist()

    row = st.columns(4)
    row[0].metric("Revenue", format_rupiah(revenue(df)))
    row[1].metric("Orders", format_int(orders(df)))
    row[2].metric("Metode Pembayaran", format_int(len(payment)))
    row[3].metric("Total Diskon", format_rupiah(discount["total_discount"]))

    st.subheader("Performa Metode Pembayaran")
    st.caption(
        "Menggunakan kolom kanonik `Metode_Pembayaran_Clean` (13 kategori). Urutan "
        "berdasarkan **Revenue** menurun. Diskon ditampilkan sebagai nilai agregat "
        "(`Total Diskon`), **bukan** rasio terhadap revenue."
    )
    st.plotly_chart(_payment_revenue_figure(payment), use_container_width=True)
    st.dataframe(
        _payment_table(payment.reset_index(drop=True)),
        use_container_width=True,
        hide_index=True,
    )

    if zero_revenue_methods:
        st.info(
            "Metode dengan Revenue Rp0 pada cakupan ini (tetap memiliki order): "
            + ", ".join(zero_revenue_methods)
            + ". Nilai Rp0 berasal dari data, bukan hasil imputasi."
        )

    st.subheader("Diskon")
    st.plotly_chart(_payment_discount_figure(payment), use_container_width=True)

    col = st.columns(3)
    col[0].metric("Total Diskon", format_rupiah(discount["total_discount"]))
    col[1].metric("Order dengan diskon > 0", format_int(discount["orders_with_discount"]))
    col[2].metric("Order tanpa diskon (Rp0)", format_int(discount["orders_without_discount"]))

    if discount["missing_discount"]:
        st.warning(
            f"Terdapat {format_int(discount['missing_discount'])} nilai `Total Diskon` "
            "kosong pada cakupan ini; nilai kosong tidak diperlakukan sebagai Rp0."
        )
    else:
        st.caption(
            "Kolom `Total Diskon` tidak memiliki nilai kosong pada dataset ini, "
            "sehingga Rp0 berarti memang tidak ada diskon, bukan data hilang. "
            "Discount Rate tidak ditampilkan karena denominatornya belum disetujui."
        )
