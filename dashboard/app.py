from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st

from src.data_loader import get_dataset
from src.formatting import format_int
from src.metrics import apply_filters, calendar_month_range
from src.pages import (
    executive_overview,
    order_operations,
    payment_discount,
    product_regional,
    shipping_data_quality,
)

st.set_page_config(
    page_title="Data Analyst Dashboard",
    page_icon="📊",
    layout="wide",
)

PAGES = {
    "Executive Overview": executive_overview.render,
    "Product & Regional Analysis": product_regional.render,
    "Payment & Discount": payment_discount.render,
    "Order Operations": order_operations.render,
    "Shipping & Data Quality": shipping_data_quality.render,
}

st.title("Data Analyst Dashboard — Indonesia E-Commerce Sales")

try:
    full_df = get_dataset()
    load_ok = True
except Exception as exc:
    load_ok = False
    st.error(f"Gagal memuat dataset: {exc}")

if load_ok:
    st.sidebar.success(
        f"Dataset: {format_int(full_df.shape[0])} baris × {full_df.shape[1]} kolom"
    )

    page_name = st.sidebar.radio("Navigasi", list(PAGES.keys()))

    st.sidebar.divider()
    st.sidebar.subheader("Filter")

    min_date = full_df["order_datetime"].min().date()
    max_date = full_df["order_datetime"].max().date()
    date_selection = st.sidebar.date_input(
        "Rentang tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
    if isinstance(date_selection, (list, tuple)):
        if len(date_selection) == 2:
            start_date, end_date = date_selection
        elif len(date_selection) == 1:
            start_date = end_date = date_selection[0]
        else:
            start_date, end_date = min_date, max_date
    else:
        start_date = end_date = date_selection

    province_options = sorted(full_df["Provinsi"].dropna().unique().tolist())
    selected_provinces = st.sidebar.multiselect(
        "Provinsi (kosong = semua)",
        options=province_options,
        default=[],
    )

    filtered_df = apply_filters(
        full_df,
        start_date=start_date,
        end_date=end_date,
        provinces=selected_provinces,
    )

    st.sidebar.caption(
        f"Menampilkan {format_int(filtered_df.shape[0])} dari "
        f"{format_int(full_df.shape[0])} order."
    )

    trend_start, trend_end = calendar_month_range(full_df)

    PAGES[page_name](filtered_df, full_df, trend_start, trend_end)
