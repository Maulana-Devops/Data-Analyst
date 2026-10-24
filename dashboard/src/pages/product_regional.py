from __future__ import annotations

import pandas as pd
import streamlit as st

from src.charts import PRIMARY_COLOR, bar_chart, empty_figure
from src.formatting import format_int, format_percent, format_rupiah
from src.metrics import (
    CATEGORY_COLUMN,
    PROVINCE_COLUMN,
    category_summary,
    orders,
    province_summary,
    revenue,
)

TOP_N_OPTIONS = [5, 10, 15, 20]


def _category_figure(summary: pd.DataFrame, top_n: int):
    top = summary.head(top_n)
    return bar_chart(
        top[CATEGORY_COLUMN],
        top["Revenue"],
        title=f"Top {top_n} Kategori berdasarkan Revenue",
        category_title="Kategori produk",
        value_title="Revenue",
        value_formatter=format_rupiah,
        orientation="h",
        height=max(360, 28 * len(top) + 120),
    )


def _province_figure(summary: pd.DataFrame, top_n: int):
    top = summary.head(top_n)
    return bar_chart(
        top[PROVINCE_COLUMN],
        top["Revenue"],
        title=f"Top {top_n} Provinsi berdasarkan Revenue",
        category_title="Provinsi",
        value_title="Revenue",
        value_formatter=format_rupiah,
        orientation="h",
        color=PRIMARY_COLOR,
        height=max(360, 28 * len(top) + 120),
    )


def _contribution_table(summary: pd.DataFrame, label_column: str, total_revenue: float):
    table = summary.copy()
    table["Kontribusi Revenue"] = [
        (value / total_revenue if total_revenue else 0.0) for value in table["Revenue"]
    ]
    display = pd.DataFrame(
        {
            label_column: table[label_column],
            "Revenue": table["Revenue"].map(format_rupiah),
            "Kontribusi Revenue": table["Kontribusi Revenue"].map(format_percent),
            "Orders": table["Orders"].map(format_int),
            "Quantity": table["Quantity"].map(format_int),
            "AOV": table["AOV"].map(lambda value: format_rupiah(value, 2)),
        }
    )
    return display


def render(df: pd.DataFrame, full_df: pd.DataFrame, start=None, end=None) -> None:
    st.header("Product & Regional Analysis")

    total_revenue = revenue(df)
    total_orders = orders(df)

    if df.empty:
        st.warning("Tidak ada data pada filter saat ini.")
        st.plotly_chart(empty_figure(), use_container_width=True)
        return

    categories = category_summary(df)
    provinces = province_summary(df)

    nonzero_categories = int((categories["Revenue"] > 0).sum())
    zero_categories = int((categories["Revenue"] == 0).sum())

    row = st.columns(4)
    row[0].metric("Revenue", format_rupiah(total_revenue))
    row[1].metric("Orders", format_int(total_orders))
    row[2].metric("Kategori (revenue > 0)", format_int(nonzero_categories))
    row[3].metric("Provinsi", format_int(len(provinces)))

    top_n = st.selectbox("Jumlah kategori/provinsi teratas (Top N)", TOP_N_OPTIONS, index=1)
    st.caption(
        "Urutan Top N menggunakan **Revenue** (`Total Pembayaran`) secara menurun; "
        "nilai yang sama dipakai untuk mengurutkan tabel."
    )

    st.subheader("Kategori Produk")
    st.plotly_chart(_category_figure(categories, top_n), use_container_width=True)
    st.markdown(f"**Top {min(top_n, len(categories))} kategori — ringkasan**")
    st.dataframe(
        _contribution_table(categories.head(top_n), CATEGORY_COLUMN, total_revenue),
        use_container_width=True,
        hide_index=True,
    )
    if zero_categories:
        st.caption(
            f"Sebanyak {format_int(zero_categories)} kategori memiliki Revenue Rp0 pada "
            "cakupan filter ini (tetap ditampilkan pada tabel lengkap, tidak "
            "diasumsikan sama dengan tidak ada order)."
        )

    st.subheader("Provinsi")
    st.plotly_chart(_province_figure(provinces, top_n), use_container_width=True)
    st.markdown(f"**Top {min(top_n, len(provinces))} provinsi — ringkasan**")
    st.dataframe(
        _contribution_table(provinces.head(top_n), PROVINCE_COLUMN, total_revenue),
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("Tabel lengkap (semua kategori & provinsi)"):
        st.markdown("**Semua kategori (urut Revenue menurun)**")
        st.dataframe(
            _contribution_table(categories, CATEGORY_COLUMN, total_revenue),
            use_container_width=True,
            hide_index=True,
        )
        st.markdown("**Semua provinsi (urut Revenue menurun)**")
        st.dataframe(
            _contribution_table(provinces, PROVINCE_COLUMN, total_revenue),
            use_container_width=True,
            hide_index=True,
        )
        st.caption(
            "Kontribusi Revenue = Revenue kategori/provinsi ÷ total Revenue pada "
            "cakupan filter. Revenue dihitung dari `Total Pembayaran`; Orders "
            "menghitung `order_id` unik; Quantity menjumlahkan `total_qty` tanpa "
            "imputasi nilai kosong. Dataset ini sintetis; angka tidak menyiratkan "
            "sebab-akibat performa pasar."
        )
