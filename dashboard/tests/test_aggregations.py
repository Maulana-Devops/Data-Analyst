from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_loader import get_dataset
from src import metrics


class TestFiltersAndTrend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()
        cls.trend_start, cls.trend_end = metrics.calendar_month_range(cls.df)

    def test_full_filter_is_identity(self):
        filtered = metrics.apply_filters(
            self.df,
            start_date=self.df["order_datetime"].min().date(),
            end_date=self.df["order_datetime"].max().date(),
        )
        self.assertEqual(filtered.shape[0], 18868)
        self.assertEqual(round(metrics.revenue(filtered)), 962091801)

    def test_province_filter_revenue(self):
        filtered = metrics.apply_filters(self.df, provinces=["JAWA BARAT"])
        self.assertEqual(round(metrics.revenue(filtered)), 247638372)
        self.assertEqual(metrics.orders(filtered), 6078)

    def test_date_filter_revenue(self):
        filtered = metrics.apply_filters(
            self.df,
            start_date="2024-07-01",
            end_date="2024-07-31",
        )
        self.assertEqual(round(metrics.revenue(filtered)), 63791545)
        self.assertEqual(metrics.orders(filtered), 1270)

    def test_filter_rates_use_filtered_denominator(self):
        filtered = metrics.apply_filters(self.df, provinces=["BANTEN"])
        expected_orders = int((self.df["Provinsi"] == "BANTEN").sum())
        self.assertEqual(metrics.orders(filtered), expected_orders)
        expected_cancelled = int(
            ((self.df["Provinsi"] == "BANTEN") & (self.df["Is_Cancelled"] == True)).sum()
        )
        self.assertEqual(metrics.cancelled_orders(filtered), expected_cancelled)
        self.assertAlmostEqual(
            metrics.cancellation_rate(filtered),
            expected_cancelled / expected_orders,
            places=9,
        )

    def test_missing_qty_preserved_after_filter(self):
        province = "JAWA BARAT"
        filtered = metrics.apply_filters(self.df, provinces=[province])
        manual = int(
            (
                (self.df["Provinsi"] == province)
                & (self.df["total_qty"].isna())
            ).sum()
        )
        self.assertEqual(metrics.missing_quantity_count(filtered), manual)
        self.assertGreaterEqual(manual, 0)

    def test_trend_covers_full_calendar(self):
        trend = metrics.monthly_revenue_trend(
            self.df, start=self.trend_start, end=self.trend_end
        )
        self.assertEqual(len(trend), 24)
        self.assertEqual(int(trend["Has_Transactions"].sum()), 22)

    def test_trend_total_revenue_matches_dataset(self):
        trend = metrics.monthly_revenue_trend(
            self.df, start=self.trend_start, end=self.trend_end
        )
        self.assertEqual(round(trend["Revenue"].sum()), 962091801)
        self.assertEqual(round(trend["Orders"].sum()), 18868)

    def test_known_missing_months(self):
        self.assertEqual(
            metrics.missing_months(self.df, start=self.trend_start, end=self.trend_end),
            ["2024-12", "2025-07"],
        )

    def test_missing_months_are_not_zero(self):
        trend = metrics.monthly_revenue_trend(
            self.df, start=self.trend_start, end=self.trend_end
        )
        for month in ["2024-12", "2025-07"]:
            row = trend.loc[trend["Periode"] == month].iloc[0]
            self.assertFalse(bool(row["Has_Transactions"]))
            self.assertTrue(pd.isna(row["Revenue"]))
            self.assertTrue(pd.isna(row["AOV"]))

    def test_trend_aov_matches_revenue_over_orders(self):
        trend = metrics.monthly_revenue_trend(
            self.df, start=self.trend_start, end=self.trend_end
        )
        for _, row in trend.dropna(subset=["Revenue"]).iterrows():
            self.assertAlmostEqual(
                row["AOV"], row["Revenue"] / row["Orders"], places=6
            )

    def test_province_trend_gaps_are_nan(self):
        filtered = metrics.apply_filters(self.df, provinces=["PAPUA"])
        trend = metrics.monthly_revenue_trend(
            filtered, start=self.trend_start, end=self.trend_end
        )
        self.assertEqual(len(trend), 24)
        self.assertGreater(int((~trend["Has_Transactions"]).sum()), 0)
        self.assertTrue(trend["Revenue"].isna().any())


if __name__ == "__main__":
    unittest.main(verbosity=2)
