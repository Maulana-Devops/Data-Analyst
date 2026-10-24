from __future__ import annotations

from pathlib import Path

import pandas as pd

DATE_COLUMNS = ["order_datetime", "order_date_clean"]
NUMERIC_COLUMNS = [
    "total_qty",
    "total_weight_gr",
    "total_returned_qty",
    "Total Diskon",
    "num_product_categories",
    "Ongkos Kirim Dibayar oleh Pembeli",
    "Estimasi Potongan Biaya Pengiriman",
    "Total Pembayaran",
    "Perkiraan Ongkos Kirim",
    "Tahun",
    "Bulan",
]
BOOLEAN_COLUMNS = ["Is_Cancelled", "Is_Returned"]

DATASET_RELATIVE_PATH = Path(
    "docs/Final Project/02_Data/Clean_Dataset/Clean_Dataset.csv"
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def resolve_dataset_path(path: Path | str | None = None) -> Path:
    if path is None:
        return repo_root() / DATASET_RELATIVE_PATH
    return Path(path).expanduser().resolve()


def _to_boolean(series: pd.Series) -> pd.Series:
    normalized = series.astype("string").str.strip().str.lower()
    return normalized.map({"true": True, "false": False}).astype("boolean")


def load_dataset(path: Path | str | None = None) -> pd.DataFrame:
    dataset_path = resolve_dataset_path(path)
    if not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    df = pd.read_csv(dataset_path, sep=";", encoding="utf-8-sig")

    for column in DATE_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    for column in NUMERIC_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    for column in BOOLEAN_COLUMNS:
        if column in df.columns:
            df[column] = _to_boolean(df[column])

    return df


_CACHED_LOADER = None


def get_dataset(path: Path | str | None = None) -> pd.DataFrame:
    global _CACHED_LOADER
    if _CACHED_LOADER is None:
        try:
            import streamlit as st

            _CACHED_LOADER = st.cache_data(show_spinner=False)(load_dataset)
        except Exception:
            _CACHED_LOADER = load_dataset
    return _CACHED_LOADER(path)
