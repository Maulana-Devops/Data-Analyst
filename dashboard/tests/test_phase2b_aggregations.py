from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import metrics
from src.charts import bar_chart, empty_figure
from src.data_loader import get_dataset
from src.pages import (
    order_operations,
    payment_discount,
    product_regional,
    shipping_data_quality,
)

PROVINCE_FILTER = "JAWA BARAT"
PROVINCE_REVENUE = 247638372
PROVINCE_ORDERS = 6078


class TestCategoryAndProvinceAggregation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_category_revenue_reconciles(self):
        summary = metrics.category_summary(self.df)
        self.assertEqual(round(summary["Revenue"].sum()), metrics.revenue(self.df))

    def test_category_orders_reconcile_without_double_counting(self):
        summary = metrics.category_summary(self.df)
        self.assertEqual(int(summary["Orders"].sum()), metrics.orders(self.df))

    def test_category_sorted_by_revenue_desc(self):
        summary = metrics.category_summary(self.df)
        self.assertTrue(summary["Revenue"].is_monotonic_decreasing)

    def test_zero_revenue_categories_retained(self):
        summary = metrics.category_summary(self.df)
        self.assertEqual(int((summary["Revenue"] == 0).sum()), 55)
        self.assertEqual(len(summary), 640)

    def test_province_revenue_reconciles(self):
        summary = metrics.province_summary(self.df)
        self.assertEqual(round(summary["Revenue"].sum()), metrics.revenue(self.df))

    def test_province_orders_reconcile(self):
        summary = metrics.province_summary(self.df)
        self.assertEqual(int(summary["Orders"].sum()), metrics.orders(self.df))

    def test_province_filter_changes_aggregation(self):
        filtered = metrics.apply_filters(self.df, provinces=[PROVINCE_FILTER])
        summary = metrics.category_summary(filtered)
        self.assertEqual(round(summary["Revenue"].sum()), PROVINCE_REVENUE)
        self.assertEqual(int(summary["Orders"].sum()), PROVINCE_ORDERS)


class TestPaymentAggregation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_payment_categories_count(self):
        summary = metrics.payment_summary(self.df)
        self.assertEqual(len(summary), 13)

    def test_payment_revenue_reconciles(self):
        summary = metrics.payment_summary(self.df)
        self.assertEqual(round(summary["Revenue"].sum()), metrics.revenue(self.df))

    def test_payment_orders_reconcile_no_duplication(self):
        summary = metrics.payment_summary(self.df)
        self.assertEqual(int(summary["Orders"].sum()), metrics.orders(self.df))

    def test_payment_discount_matches_manual_total(self):
        summary = metrics.payment_summary(self.df)
        self.assertEqual(round(summary["Discount"].sum()), 8004196)

    def test_zero_revenue_methods_present(self):
        summary = metrics.payment_summary(self.df)
        zero = set(summary.loc[summary["Revenue"] == 0, metrics.PAYMENT_COLUMN])
        self.assertEqual(zero, {"Pembayaran dibebaskan", "Mitra Shopee"})

    def test_payment_filter_reconciles(self):
        filtered = metrics.apply_filters(self.df, provinces=[PROVINCE_FILTER])
        summary = metrics.payment_summary(filtered)
        self.assertEqual(int(summary["Orders"].sum()), PROVINCE_ORDERS)
        self.assertEqual(round(summary["Revenue"].sum()), PROVINCE_REVENUE)


class TestStatusAndCancellation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_status_orders_reconcile(self):
        summary = metrics.status_summary(self.df)
        self.assertEqual(len(summary), 4)
        self.assertEqual(int(summary["Orders"].sum()), metrics.orders(self.df))

    def test_status_share_denominator_is_total_orders(self):
        summary = metrics.status_summary(self.df)
        total = metrics.orders(self.df)
        self.assertAlmostEqual(float(summary["Share"].sum()), 1.0, places=9)
        for _, row in summary.iterrows():
            self.assertAlmostEqual(row["Share"], row["Orders"] / total, places=12)

    def test_cancellation_reasons_sum_to_cancelled_orders(self):
        summary = metrics.cancellation_reason_summary(self.df)
        self.assertEqual(int(summary["Orders"].sum()), metrics.cancelled_orders(self.df))
        self.assertEqual(int(summary["Orders"].sum()), 2573)

    def test_cancellation_excludes_non_cancelled_rows(self):
        summary = metrics.cancellation_reason_summary(self.df)
        self.assertNotIn("Tidak dibatalkan", set(summary["Alasan"]))

    def test_cancellation_filter_reconciles(self):
        filtered = metrics.apply_filters(self.df, provinces=["BANTEN"])
        summary = metrics.cancellation_reason_summary(filtered)
        self.assertEqual(int(summary["Orders"].sum()), metrics.cancelled_orders(filtered))


class TestReturnsAggregation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_returned_orders_by_category_reconcile(self):
        summary = metrics.returns_summary(self.df, metrics.CATEGORY_COLUMN)
        self.assertEqual(int(summary["ReturnedOrders"].sum()), metrics.returned_orders(self.df))

    def test_returned_quantity_by_category_reconcile(self):
        summary = metrics.returns_summary(self.df, metrics.CATEGORY_COLUMN)
        self.assertEqual(round(summary["ReturnedQuantity"].sum()), 353)

    def test_orders_and_units_are_distinct(self):
        summary = metrics.returns_summary(self.df, metrics.PROVINCE_COLUMN)
        self.assertNotEqual(
            int(summary["ReturnedOrders"].sum()),
            int(summary["ReturnedQuantity"].sum()),
        )

    def test_order_return_rate_definition(self):
        summary = metrics.returns_summary(self.df, metrics.CATEGORY_COLUMN)
        for _, row in summary.iterrows():
            expected = row["ReturnedOrders"] / row["TotalOrders"] if row["TotalOrders"] else 0
            self.assertAlmostEqual(row["OrderReturnRate"], expected, places=12)

    def test_total_orders_per_group_matches_grouping(self):
        summary = metrics.returns_summary(self.df, metrics.PROVINCE_COLUMN)
        self.assertEqual(int(summary["TotalOrders"].sum()), metrics.orders(self.df))


class TestShippingDiscountQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_discount_summary_no_missing(self):
        summary = metrics.discount_summary(self.df)
        self.assertEqual(summary["missing_discount"], 0)
        self.assertEqual(round(summary["total_discount"]), 8004196)
        self.assertEqual(summary["orders_with_discount"], 126)

    def test_shipping_totals_match_manual(self):
        summary = metrics.shipping_summary(self.df)
        self.assertEqual(round(summary["paid_by_buyer"]["total"]), 81365659)
        self.assertEqual(round(summary["subsidy_estimate"]["total"]), 200109075)
        self.assertEqual(round(summary["cost_estimate"]["total"]), 348049366)

    def test_shipping_has_no_missing_values(self):
        summary = metrics.shipping_summary(self.df)
        for key in ("paid_by_buyer", "subsidy_estimate", "cost_estimate"):
            self.assertEqual(summary[key]["missing"], 0)

    def test_shipping_method_orders_reconcile(self):
        summary = metrics.shipping_method_summary(self.df)
        self.assertEqual(int(summary["Orders"].sum()), metrics.orders(self.df))

    def test_missing_quantity_preserved(self):
        self.assertEqual(metrics.missing_quantity_count(self.df), 283)

    def test_missing_value_summary_reports_real_missing_columns(self):
        summary = metrics.missing_value_summary(self.df)
        counts = dict(zip(summary["Kolom"], summary["Jumlah Missing"]))
        self.assertEqual(
            counts, {"total_qty": 283, "Metode Pembayaran": 283, "order_date": 188}
        )


class TestMissingValuesNotCoercedToZero(unittest.TestCase):
    def test_quantity_all_missing_group_stays_nan(self):
        frame = pd.DataFrame(
            {
                "product_categories": ["A", "B"],
                "order_id": ["o1", "o2"],
                "Total Pembayaran": [10.0, 20.0],
                "total_qty": [float("nan"), float("nan")],
            }
        )
        summary = metrics.category_summary(frame)
        self.assertTrue(summary["Quantity"].isna().all())

    def test_partial_missing_quantity_skips_only_missing(self):
        frame = pd.DataFrame(
            {
                "product_categories": ["A", "A"],
                "order_id": ["o1", "o2"],
                "Total Pembayaran": [10.0, 20.0],
                "total_qty": [5.0, float("nan")],
            }
        )
        summary = metrics.category_summary(frame)
        self.assertEqual(float(summary["Quantity"].iloc[0]), 5.0)

    def test_shipping_all_missing_stays_nan(self):
        frame = pd.DataFrame(
            {
                metrics.SHIPPING_PAID_COLUMN: [float("nan")],
                metrics.SHIPPING_SUBSIDY_COLUMN: [float("nan")],
                metrics.SHIPPING_ESTIMATE_COLUMN: [float("nan")],
            }
        )
        summary = metrics.shipping_summary(frame)
        self.assertTrue(pd.isna(summary["paid_by_buyer"]["total"]))
        self.assertEqual(summary["paid_by_buyer"]["missing"], 1)

    def test_discount_all_missing_stays_nan(self):
        frame = pd.DataFrame({metrics.DISCOUNT_COLUMN: [float("nan"), float("nan")]})
        summary = metrics.discount_summary(frame)
        self.assertTrue(pd.isna(summary["total_discount"]))
        self.assertEqual(summary["missing_discount"], 2)


class TestEmptyInputs(unittest.TestCase):
    def test_aggregations_return_empty_with_columns(self):
        empty = pd.DataFrame()
        self.assertTrue(metrics.category_summary(empty).empty)
        self.assertTrue(metrics.province_summary(empty).empty)
        self.assertTrue(metrics.payment_summary(empty).empty)
        self.assertTrue(metrics.status_summary(empty).empty)
        self.assertTrue(metrics.cancellation_reason_summary(empty).empty)
        self.assertTrue(metrics.returns_summary(empty, metrics.CATEGORY_COLUMN).empty)
        self.assertTrue(metrics.shipping_method_summary(empty).empty)
        self.assertTrue(metrics.missing_value_summary(empty).empty)

    def test_scalar_summaries_on_empty(self):
        self.assertEqual(metrics.discount_summary(pd.DataFrame())["total_discount"], 0.0)
        shipping = metrics.shipping_summary(pd.DataFrame())
        self.assertEqual(shipping["paid_by_buyer"]["total"], 0.0)

    def test_figures_handle_empty(self):
        self.assertIsInstance(empty_figure(), go.Figure)
        self.assertIsInstance(bar_chart([], [], title="x", category_title="a", value_title="b"), go.Figure)


class TestPageFigures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_product_figures(self):
        categories = metrics.category_summary(self.df)
        provinces = metrics.province_summary(self.df)
        self.assertIsInstance(product_regional._category_figure(categories, 10), go.Figure)
        self.assertIsInstance(product_regional._province_figure(provinces, 10), go.Figure)

    def test_payment_figures(self):
        payment = metrics.payment_summary(self.df)
        self.assertIsInstance(payment_discount._payment_revenue_figure(payment), go.Figure)
        self.assertIsInstance(payment_discount._payment_discount_figure(payment), go.Figure)

    def test_order_operations_figures(self):
        status = metrics.status_summary(self.df)
        reasons = metrics.cancellation_reason_summary(self.df)
        returns = metrics.returns_summary(self.df, metrics.CATEGORY_COLUMN)
        self.assertIsInstance(order_operations._status_figure(status), go.Figure)
        self.assertIsInstance(order_operations._cancellation_figure(reasons, 10), go.Figure)
        self.assertIsInstance(
            order_operations._returns_figure(returns, metrics.CATEGORY_COLUMN, 10), go.Figure
        )

    def test_shipping_figures(self):
        shipping = metrics.shipping_summary(self.df)
        methods = metrics.shipping_method_summary(self.df)
        self.assertIsInstance(
            shipping_data_quality._shipping_comparison_figure(shipping, metrics.revenue(self.df)),
            go.Figure,
        )
        self.assertIsInstance(
            shipping_data_quality._shipping_method_figure(methods, 10), go.Figure
        )


class TestForbiddenMetricsGuard(unittest.TestCase):
    def test_metrics_module_exposes_no_forbidden_rates(self):
        self.assertFalse(hasattr(metrics, "discount_rate"))
        self.assertFalse(hasattr(metrics, "quantity_return_rate"))

    def test_source_defines_no_forbidden_rate_functions(self):
        src_dir = Path(__file__).resolve().parents[1] / "src"
        offenders = []
        for path in src_dir.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            if "def discount_rate" in text or "def quantity_return_rate" in text:
                offenders.append(path.name)
        self.assertEqual(offenders, [])

    def test_kpi_reference_values_unchanged(self):
        df = get_dataset()
        kpi = metrics.kpi_summary(df)
        self.assertEqual(round(kpi["revenue"]), 962091801)
        self.assertEqual(kpi["orders"], 18868)
        self.assertEqual(round(kpi["total_unit_tercatat"]), 47688)
        self.assertEqual(kpi["cancelled_orders"], 2573)
        self.assertEqual(kpi["returned_orders"], 143)


if __name__ == "__main__":
    unittest.main(verbosity=2)
