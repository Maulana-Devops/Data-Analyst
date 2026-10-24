from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_loader import get_dataset
from src import metrics


class TestDatasetAndMetrics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = get_dataset()

    def test_dimensions(self):
        self.assertEqual(self.df.shape[0], 18868)
        self.assertEqual(self.df.shape[1], 30)

    def test_order_id_unique(self):
        self.assertEqual(self.df["order_id"].duplicated().sum(), 0)
        self.assertEqual(self.df["order_id"].nunique(), 18868)

    def test_revenue(self):
        self.assertEqual(round(metrics.revenue(self.df)), 962091801)

    def test_orders(self):
        self.assertEqual(metrics.orders(self.df), 18868)

    def test_total_unit_tercatat(self):
        self.assertEqual(round(metrics.total_unit_tercatat(self.df)), 47688)

    def test_aov(self):
        self.assertAlmostEqual(metrics.aov(self.df), 50990.66149035404, places=3)

    def test_cancelled_orders(self):
        self.assertEqual(metrics.cancelled_orders(self.df), 2573)

    def test_cancellation_rate(self):
        self.assertAlmostEqual(metrics.cancellation_rate(self.df), 0.136368, places=5)

    def test_returned_orders(self):
        self.assertEqual(metrics.returned_orders(self.df), 143)

    def test_order_return_rate(self):
        self.assertAlmostEqual(metrics.order_return_rate(self.df), 0.007579, places=6)

    def test_returned_quantity(self):
        self.assertEqual(round(metrics.returned_quantity(self.df)), 353)

    def test_total_qty_missing_preserved(self):
        self.assertEqual(int(self.df["total_qty"].isna().sum()), 283)

    def test_payment_categories(self):
        self.assertEqual(self.df[metrics.PAYMENT_COLUMN].nunique(), 13)

    def test_status_categories(self):
        self.assertEqual(self.df[metrics.STATUS_COLUMN].nunique(), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
