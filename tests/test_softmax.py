import unittest
import numpy as np
from chapter03.softmax import softmax


class SoftmaxTestCase(unittest.TestCase):
    """softmax をテストするテストケース"""

    def test_representative(self):
        expected = 1
        actual = softmax(3)
        self.assertEqual(expected, actual)

    def test_supports_ndarray(self):
        expected = np.array([0.018211, 0.245191, 0.736596])
        actual = softmax(np.array([0.3, 2.9, 4.0]))
        np.testing.assert_allclose(expected, actual, atol=1e-6)
