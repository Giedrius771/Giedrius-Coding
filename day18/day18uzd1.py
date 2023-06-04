import unittest


def refine_sum(*args):
    return round(sum(args), 2)


def refund_amount(num_list):
    return sum(num_list)


def print_largest_number(*args):
    return max(args)


class TestFunctions(unittest.TestCase):
    def test_refine_sum(self):
        self.assertEqual(refine_sum(3, 2, 1), 6)
        self.assertAlmostEqual(refine_sum(0.1, 0.2, 0.3), 0.6)
        self.assertEqual(refine_sum(-1, -2, -3), -6)

    def test_refund_amount(self):
        self.assertEqual(refund_amount([10, 20, 30]), 60)
        self.assertAlmostEqual(refund_amount([0.1, 0.2, 0.3]), 0.6)
        self.assertEqual(refund_amount([-10, -20, -30]), -60)

    def test_print_largest_number(self):
        self.assertEqual(print_largest_number(10, 20, 30, 40), 40)
        self.assertEqual(print_largest_number(-10, -20, -5), -5)
        self.assertAlmostEqual(print_largest_number(0.1, 0.5, 0.2), 0.5)


if __name__ == '__main__':
    unittest.main()
