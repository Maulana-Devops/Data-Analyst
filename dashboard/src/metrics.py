from __future__ import annotations

import pandas as pd

PAYMENT_COLUMN = "Metode_Pembayaran_Clean"
STATUS_COLUMN = "Status_Analisis"
ORDER_COLUMN = "order_id"


def safe_div(numerator: float, denominator: float) -> float:
    if denominator in (0, None) or pd.isna(denominator):
        return 0.0
    return float(numerator) / float(denominator)


def revenue(df: pd.DataFrame) -> float:
    return float(df["Total Pembayaran"].sum())


def orders(df: pd.DataFrame) -> int:
    return int(df[ORDER_COLUMN].nunique())


def total_unit_tercatat(df: pd.DataFrame) -> float:
    return float(df["total_qty"].sum())


def aov(df: pd.DataFrame) -> float:
    return safe_div(revenue(df), orders(df))


def cancelled_orders(df: pd.DataFrame) -> int:
    return int((df["Is_Cancelled"] == True).sum())


def cancellation_rate(df: pd.DataFrame) -> float:
    return safe_div(cancelled_orders(df), orders(df))


def returned_orders(df: pd.DataFrame) -> int:
    return int((df["Is_Returned"] == True).sum())


def order_return_rate(df: pd.DataFrame) -> float:
    return safe_div(returned_orders(df), orders(df))


def returned_quantity(df: pd.DataFrame) -> float:
    return float(df["total_returned_qty"].sum())


def kpi_summary(df: pd.DataFrame) -> dict[str, float]:
    total_orders = orders(df)
    return {
        "revenue": revenue(df),
        "orders": total_orders,
        "total_unit_tercatat": total_unit_tercatat(df),
        "aov": aov(df),
        "cancelled_orders": cancelled_orders(df),
        "cancellation_rate": cancellation_rate(df),
        "returned_orders": returned_orders(df),
        "order_return_rate": order_return_rate(df),
        "returned_quantity": returned_quantity(df),
    }


def missing_quantity_count(df: pd.DataFrame) -> int:
    return int(df["total_qty"].isna().sum())


def apply_filters(
    df: pd.DataFrame,
    start_date=None,
    end_date=None,
    provinces=None,
) -> pd.DataFrame:
    result = df
    if start_date is not None:
        result = result[result["order_datetime"] >= pd.Timestamp(start_date)]
    if end_date is not None:
        end_exclusive = pd.Timestamp(end_date) + pd.DateOffset(days=1)
        result = result[result["order_datetime"] < end_exclusive]
    if provinces is not None:
        selected = list(provinces)
        if selected:
            result = result[result["Provinsi"].isin(selected)]
    return result


def calendar_month_range(df: pd.DataFrame):
    valid = df["order_datetime"].dropna()
    if valid.empty:
        return None, None
    return valid.min().to_period("M"), valid.max().to_period("M")


TREND_COLUMNS = ["Periode", "Revenue", "Orders", "Quantity", "AOV", "Has_Transactions"]


def monthly_revenue_trend(df: pd.DataFrame, start=None, end=None) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=TREND_COLUMNS)

    data = df.dropna(subset=["order_datetime"]).copy()
    if data.empty:
        return pd.DataFrame(columns=TREND_COLUMNS)

    data["Periode"] = data["order_datetime"].dt.to_period("M")
    grouped = data.groupby("Periode", sort=True).agg(
        Revenue=("Total Pembayaran", "sum"),
        Orders=("order_id", "nunique"),
        Quantity=("total_qty", "sum"),
    )

    data_start, data_end = calendar_month_range(df)
    start = start if start is not None else data_start
    end = end if end is not None else data_end

    full = pd.period_range(start, end, freq="M")
    grouped = grouped.reindex(full)
    grouped.index.name = "Periode"
    grouped = grouped.reset_index()

    grouped["Has_Transactions"] = grouped["Revenue"].notna()
    grouped["AOV"] = [
        safe_div(rev, ordr)
        if pd.notna(rev) and pd.notna(ordr) and ordr
        else float("nan")
        for rev, ordr in zip(grouped["Revenue"], grouped["Orders"])
    ]
    grouped["Periode"] = grouped["Periode"].astype(str)
    return grouped[TREND_COLUMNS]


def missing_months(df: pd.DataFrame, start=None, end=None) -> list[str]:
    trend = monthly_revenue_trend(df, start=start, end=end)
    if trend.empty:
        return []
    return trend.loc[~trend["Has_Transactions"], "Periode"].tolist()


CATEGORY_COLUMN = "product_categories"
PROVINCE_COLUMN = "Provinsi"
CANCELLATION_REASON_COLUMN = "Alasan Pembatalan"
SHIPPING_METHOD_COLUMN = "Opsi Pengiriman"
DISCOUNT_COLUMN = "Total Diskon"
SHIPPING_PAID_COLUMN = "Ongkos Kirim Dibayar oleh Pembeli"
SHIPPING_SUBSIDY_COLUMN = "Estimasi Potongan Biaya Pengiriman"
SHIPPING_ESTIMATE_COLUMN = "Perkiraan Ongkos Kirim"

SUMMARY_COLUMNS = ["Revenue", "Orders", "Quantity", "AOV"]


def order_summary(
    df: pd.DataFrame,
    by: str,
    extra_sums: dict[str, str] | None = None,
) -> pd.DataFrame:
    """Aggregate order-level metrics by a dimension without double counting.

    `Orders` counts unique `order_id`; `Revenue` sums `Total Pembayaran`;
    `Quantity` sums `total_qty` (missing values are skipped naturally and never
    filled with 0). Extra sum columns can be requested via `extra_sums`
    mapping output name -> source column.
    """
    extra_sums = extra_sums or {}
    extra_names = list(extra_sums.keys())
    columns = [by] + SUMMARY_COLUMNS + extra_names

    if df.empty:
        return pd.DataFrame(columns=columns)

    grouped = df.groupby(by, dropna=False).agg(
        Revenue=("Total Pembayaran", "sum"),
        Orders=(ORDER_COLUMN, "nunique"),
        Quantity=("total_qty", lambda values: values.sum(min_count=1)),
        **{
            name: (source, lambda values: values.sum(min_count=1))
            for name, source in extra_sums.items()
        },
    )
    grouped["AOV"] = [
        safe_div(rev, ordr) for rev, ordr in zip(grouped["Revenue"], grouped["Orders"])
    ]
    grouped = grouped.reset_index()
    return grouped[columns]


def category_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = order_summary(df, CATEGORY_COLUMN)
    return summary.sort_values("Revenue", ascending=False).reset_index(drop=True)


def province_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = order_summary(df, PROVINCE_COLUMN)
    return summary.sort_values("Revenue", ascending=False).reset_index(drop=True)


def payment_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = order_summary(df, PAYMENT_COLUMN, extra_sums={"Discount": DISCOUNT_COLUMN})
    return summary.sort_values("Revenue", ascending=False).reset_index(drop=True)


def status_summary(df: pd.DataFrame) -> pd.DataFrame:
    columns = ["Status", "Orders", "Share", "Revenue"]
    if df.empty:
        return pd.DataFrame(columns=columns)

    total_orders = orders(df)
    grouped = df.groupby(STATUS_COLUMN, dropna=False).agg(
        Orders=(ORDER_COLUMN, "nunique"),
        Revenue=("Total Pembayaran", "sum"),
    )
    grouped["Share"] = [safe_div(value, total_orders) for value in grouped["Orders"]]
    grouped = grouped.reset_index().rename(columns={STATUS_COLUMN: "Status"})
    return grouped[columns].sort_values("Orders", ascending=False).reset_index(drop=True)


def cancellation_reason_summary(df: pd.DataFrame) -> pd.DataFrame:
    columns = ["Alasan", "Orders", "Revenue"]
    if df.empty:
        return pd.DataFrame(columns=columns)

    cancelled = df[df["Is_Cancelled"] == True]
    if cancelled.empty:
        return pd.DataFrame(columns=columns)

    grouped = cancelled.groupby(CANCELLATION_REASON_COLUMN, dropna=False).agg(
        Orders=(ORDER_COLUMN, "nunique"),
        Revenue=("Total Pembayaran", "sum"),
    )
    grouped = grouped.reset_index().rename(columns={CANCELLATION_REASON_COLUMN: "Alasan"})
    return grouped[columns].sort_values("Orders", ascending=False).reset_index(drop=True)


def returns_summary(df: pd.DataFrame, by: str) -> pd.DataFrame:
    """Returned orders and returned units grouped by a dimension.

    `ReturnedOrders` counts unique returned orders (unit = order) while
    `ReturnedQuantity` sums `total_returned_qty` (unit = item); the two are
    deliberately kept separate. `OrderReturnRate` reuses the approved
    order-based definition (returned orders / orders in that group).
    """
    columns = [by, "ReturnedOrders", "ReturnedQuantity", "TotalOrders", "OrderReturnRate"]
    if df.empty:
        return pd.DataFrame(columns=columns)

    totals = df.groupby(by, dropna=False).agg(
        TotalOrders=(ORDER_COLUMN, "nunique"),
    ).reset_index()

    returned = (
        df[df["Is_Returned"] == True]
        .groupby(by, dropna=False)
        .agg(
            ReturnedOrders=(ORDER_COLUMN, "nunique"),
            ReturnedQuantity=("total_returned_qty", "sum"),
        )
        .reset_index()
    )

    merged = totals.merge(returned, on=by, how="left")
    merged["ReturnedOrders"] = merged["ReturnedOrders"].fillna(0).astype(int)
    merged["ReturnedQuantity"] = merged["ReturnedQuantity"].fillna(0.0)
    merged["OrderReturnRate"] = [
        safe_div(ro, to)
        for ro, to in zip(merged["ReturnedOrders"], merged["TotalOrders"])
    ]
    return merged[columns].sort_values("ReturnedOrders", ascending=False).reset_index(drop=True)


def discount_summary(df: pd.DataFrame) -> dict[str, float]:
    if df.empty:
        return {
            "total_discount": 0.0,
            "orders_with_discount": 0,
            "orders_without_discount": 0,
            "missing_discount": 0,
        }
    column = df[DISCOUNT_COLUMN]
    return {
        "total_discount": float(column.sum(min_count=1)),
        "orders_with_discount": int((column > 0).sum()),
        "orders_without_discount": int((column == 0).sum()),
        "missing_discount": int(column.isna().sum()),
    }


def shipping_summary(df: pd.DataFrame) -> dict[str, dict[str, float]]:
    fields = {
        "paid_by_buyer": SHIPPING_PAID_COLUMN,
        "subsidy_estimate": SHIPPING_SUBSIDY_COLUMN,
        "cost_estimate": SHIPPING_ESTIMATE_COLUMN,
    }
    result: dict[str, dict[str, float]] = {}
    for key, column in fields.items():
        if df.empty:
            result[key] = {"total": 0.0, "orders_positive": 0, "missing": 0}
            continue
        series = df[column]
        result[key] = {
            "total": float(series.sum(min_count=1)),
            "orders_positive": int((series > 0).sum()),
            "missing": int(series.isna().sum()),
        }
    return result


def shipping_method_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = order_summary(df, SHIPPING_METHOD_COLUMN)
    return summary.sort_values("Orders", ascending=False).reset_index(drop=True)


def missing_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    columns = ["Kolom", "Jumlah Missing", "Persentase"]
    if df.empty:
        return pd.DataFrame(columns=columns)

    counts = df.isna().sum()
    counts = counts[counts > 0]
    rows = [
        {
            "Kolom": column,
            "Jumlah Missing": int(count),
            "Persentase": safe_div(count, len(df)),
        }
        for column, count in counts.items()
    ]
    if not rows:
        return pd.DataFrame(columns=columns)
    return pd.DataFrame(rows).sort_values("Jumlah Missing", ascending=False).reset_index(drop=True)
