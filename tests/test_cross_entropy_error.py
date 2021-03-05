import unittest
import numpy as np
from chapter04.cross_entropy_error import cross_entropy_error


class CrossEntropyErrorTestCase(unittest.TestCase):
    """cross_entropy_error をテストするテストケース"""

    def test_representative(self):
        y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
        t = np.array([2])

        expected = 0.510826
        actual = cross_entropy_error(y, t)
        self.assertAlmostEqual(expected, actual, places=5)

    def test_supports_one_hot_label(self):
        y = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
        t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

        expected = 2.302584
        actual = cross_entropy_error(y, t)
        self.assertAlmostEqual(expected, actual, places=5)

    def test_supports_batch(self):
        y = np.array([[0.1, 0.05, 0.0, 0.6, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0],
                      [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]])
        t = np.array([3, 2])

        expected = 0.510826
        actual = cross_entropy_error(y, t)
        self.assertAlmostEqual(expected, actual, places=5)

    def test_supports_batch_one_hot_label(self):
        y = np.array([[0.1, 0.05, 0.0, 0.6, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0],
                      [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]])
        t = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])

        expected = 0.510826
        actual = cross_entropy_error(y, t)
        self.assertAlmostEqual(expected, actual, places=5)
