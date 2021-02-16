import unittest
from chapter02.nand_gate import nand_gate


class NandGateTestCase(unittest.TestCase):
    """nand_gate をテストするテストケース"""

    def test_true(self):
        expected = 1
        actual = nand_gate(0, 0)
        self.assertEqual(expected, actual)

        expected = 1
        actual = nand_gate(0, 1)
        self.assertEqual(expected, actual)

        expected = 1
        actual = nand_gate(1, 0)
        self.assertEqual(expected, actual)

    def test_false(self):
        expected = 0
        actual = nand_gate(1, 1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
