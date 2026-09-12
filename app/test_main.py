#!/usr/bin/env python3
"""Unit tests for the agentic test microservice."""

import unittest
from app.main import compute_metrics

class TestMicroservice(unittest.TestCase):
    def test_compute_metrics_keys(self):
        metrics = compute_metrics()
        self.assertIn("status", metrics)
        self.assertEqual(metrics["status"], "healthy")
        self.assertEqual(metrics["service"], "agentic-test-pipeline")
        self.assertEqual(metrics["version"], "1.0.0")

    def test_compute_metrics_types(self):
        metrics = compute_metrics()
        self.assertIsInstance(metrics, dict)
        self.assertIsInstance(metrics["version"], str)

if __name__ == "__main__":
    unittest.main()
