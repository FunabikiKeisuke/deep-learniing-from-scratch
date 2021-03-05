import unittest
import numpy as np
from chapter04.gradient_2d import numerical_gradient
from chapter04.gradient_simplenet import simpleNet


class SimpleNetTestCase(unittest.TestCase):
    """simpleNet をテストするテストケース"""

    def test_representative(self):
        x = np.array([0.6, 0.9])
        t = np.array([0, 0, 1])

        net = simpleNet()

        f = lambda w: net.loss(x, t)

        expected = np.random.randn(2, 3)
        actual = numerical_gradient(f, net.W)
        self.assertEqual(expected.shape, actual.shape)
