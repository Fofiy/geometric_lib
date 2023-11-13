import unittest

import circle
import rectangle
import square
import triangle


class CircleTests(unittest.TestCase):
    # circle.py tests
    def test_zero(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_positive_area(self):
        values = {
            1: 3.141592653589793,
            10000000: 314159265358979.3,
            100000000: 3.141592653589793e+16,
        }
        for v in values:
            self.assertEqual(circle.area(v), values[v])

    def test_positive_perimeter(self):
        values = {
            1: 6.283185307179586,
            10000000: 62831853.071795866,
            100000000: 628318530.7179586,
        }
        for v in values:
            self.assertEqual(circle.perimeter(v), values[v])

    def test_negative_area(self):
        values = [
            -1,
            -10000000,
            -91873291823
        ]
        for v in values:
            self.assertIsNone(circle.area(v))

    def test_negative_perimeter(self):
        values = [
            -1,
            -10000000,
            -91873291823
        ]
        for v in values:
            self.assertIsNone(circle.perimeter(v))

    def test_float_data_area(self):
        values = {
            1.000: 3.141592653589793,
            2.5: 19.634954084936208,
            7.123098123: 159.39978326840256,
            -123.409810923: None,
            -0.0000000000000000000000000000001: None,
            -1.0: None
        }
        for v in values:
            self.assertEqual(circle.area(v), values[v])

    def test_float_data_perimeter(self):
        values = {
            1.000: 6.283185307179586,
            2.5: 15.707963267948966,
            7.123098123: 44.75574546803209,
            -123.409810923: None,
            -0.0000000000000000000000000000001: None,
            -1.0: None
        }
        for v in values:
            self.assertEqual(circle.perimeter(v), values[v])

    def test_string_of_digits_area(self):
        values = {
            '0': 0,
            '1': 3.141592653589793,
            '10000.123987': 314167055.74024117,
            '100000000': 3.141592653589793e+16,
            '-1': None,
            '-42369903.3987': None
        }
        for v in values:
            self.assertEqual(circle.area(v), values[v])

    def test_string_of_digits_perimeter(self):
        values = {
            '0': 0,
            '1': 6.283185307179586,
            '10000000': 62831853.071795866,
            '100000000': 628318530.7179586,
            '-1': None,
            '-42369903': None
        }
        for v in values:
            self.assertEqual(circle.perimeter(v), values[v])

    def test_some_string_data(self):
        values = [
            '',
            '1a',
            'a1',
            'abc'
        ]
        for v in values:
            self.assertIsNone(circle.area(v))
            self.assertIsNone(circle.perimeter(v))


class RectangleTests(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(rectangle.area(0, 1), 0)
        self.assertEqual(rectangle.area(1, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_positive_area(self):
        values = {
            (1, 1): 1,
            (500, 400): 200000,
            (491872391, 1): 491872391
        }
        for v in values:
            self.assertEqual(rectangle.area(*v), values[v])

    def test_float_area(self):
        values = {
            (1.1, 1.1): 1.21,
            (0.0001, 10000): 1,
            (123987.1231, 5087.12039809): 630737423.0225058
        }
        for v in values:
            self.assertAlmostEqual(rectangle.area(*v), values[v])

    def test_negative_area(self):
        values = [
            (-1, 1000),
            (3192730, -1),
            (-123, 0),
            (0, -213987),
            (-13123, -987123)
        ]
        for v in values:
            self.assertIsNone(rectangle.area(*v))

    def test_str_of_digits_area(self):
        values = {
            ('2', 1): 2,
            (2, '2'): 4,
            ('3', '2'): 6,
            ('0', 234): 0,
            ('-1', 3213): None,
            (0, '-123'): None,
            (1, '54.321'): 54.321,
            ('3.22', 3): 9.66,
        }
        for v in values:
            self.assertEqual(rectangle.area(*v), values[v])

    def test_some_str_area(self):
        values = [
            ('asd', 1),
            (2, '2a'),
            ('sad1', 'iuy'),
            ('', 234),
        ]
        for v in values:
            self.assertIsNone(rectangle.area(*v))

    def test_zero_perimeter(self):
        self.assertEqual(rectangle.perimeter(0, 123), 246)
        self.assertEqual(rectangle.perimeter(123, 0), 246)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_positive_perimeter(self):
        values = {
            (1, 1): 4,
            (500, 400): 1800,
            (491872391, 1): 983744784
        }
        for v in values:
            self.assertEqual(rectangle.perimeter(*v), values[v])

    def test_float_perimeter(self):
        values = {
            (1.1, 1.1): 4.4,
            (0.0001, 10000): 20000.0002,
            (123987.1231, 5087.12039809): 258148.486996
        }
        for v in values:
            self.assertAlmostEqual(rectangle.perimeter(*v), values[v])

    def test_negative_perimeter(self):
        values = [
            (-1, 1000),
            (3192730, -1),
            (-123, 0),
            (0, -213987),
            (-13123, -987123)
        ]
        for v in values:
            self.assertIsNone(rectangle.perimeter(*v))

    def test_str_of_digits_perimeter(self):
        values = {
            ('2', 1): 6,
            (2, '2'): 8,
            ('3', '2'): 10,
            ('0', 234): 468,
            ('-1', 3213): None,
            (0, '-123'): None,
            (1, '54.321'): 110.642,
            ('3.22', 3): 12.44,
        }
        for v in values:
            self.assertEqual(rectangle.perimeter(*v), values[v])

    def test_some_str_perimeter(self):
        values = [
            ('asd', 1),
            (2, '2a'),
            ('sad1', 'iuy'),
            ('', 234),
        ]
        for v in values:
            self.assertIsNone(rectangle.perimeter(*v))


class SquareTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_positive_area(self):
        values = {
            1: 1,
            20: 400,
            17: 289
        }
        for v in values:
            self.assertEqual(square.area(v), values[v])

    def test_float_area(self):
        values = {
            1.1: 1.21,
            0.01: 0.0001,
            123987.1231: 15372806694.614553
        }
        for v in values:
            self.assertAlmostEqual(square.area(v), values[v])

    def test_negative_area(self):
        values = [
            -1,
            -123876,
            -0.0000000000000000001,
            -123098.151
        ]
        for v in values:
            self.assertIsNone(square.area(v))

    def test_str_of_digits_area(self):
        values = {
            '2': 4,
            '0': 0,
            '2.5': 6.25,
            '-1': None,
            '-123.2': None,
        }
        for v in values:
            self.assertEqual(square.area(v), values[v])

    def test_some_str_area(self):
        values = [
            ('asd', 1),
            (2, '2a'),
            ('sad1', 'iuy'),
            ('', 234),
        ]
        for v in values:
            self.assertIsNone(square.area(v))

    def test_positive_perimeter(self):
        values = {
            1: 4,
            20: 80,
            17: 68
        }
        for v in values:
            self.assertEqual(square.perimeter(v), values[v])

    def test_float_perimeter(self):
        values = {
            1.00000: 4,
            0.00000000000000001: 0.00000000000000004,
            1234129187391873987.119273987123231: 4.9365167e+18
        }
        for v in values:
            self.assertAlmostEqual(square.perimeter(v), values[v])

    def test_negative_perimeter(self):
        values = [
            -1,
            -123876,
            -0.0000000000000000001,
            -12309210938.151
        ]
        for v in values:
            self.assertIsNone(square.perimeter(v))

    def test_str_of_digits_perimeter(self):
        values = {
            '2': 8,
            '0': 0,
            '2.5': 10,
            '-1': None,
            '-123.2': None,
        }
        for v in values:
            self.assertEqual(square.perimeter(v), values[v])

    def test_some_str_perimeter(self):
        values = [
            ('asd', 1),
            (2, '2a'),
            ('sad1', 'iuy'),
            ('', 234),
        ]
        for v in values:
            self.assertIsNone(square.perimeter(v))


class TriangleTests(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(triangle.area(0, 0), 0),
        self.assertEqual(triangle.area(0, 10), 0),
        self.assertEqual(triangle.area(10, 0), 0)

    def test_positive_area(self):
        values = {
            (1, 12): 6,
            (4, 5): 10,
            (10000000000000000000, 4): 20000000000000000000
        }
        for v in values:
            self.assertEqual(triangle.area(*v), values[v])

    def test_float_area(self):
        values = {
            (1.0001, 2.42): 1.210121,
            (1987329.123056, 5987129378.123978123): 5.9491983e+15,
            (0.000, 898319231.123987): 0
        }
        for v in values:
            self.assertAlmostEqual(triangle.area(*v), values[v])

    def test_negative_area(self):
        values = [
            (-1, 123987),
            (-0.0000000000000000000001, 0),
            (142389923.12312, -1123987132987),
            (-123098.151, 228)
        ]
        for v in values:
            self.assertIsNone(triangle.area(*v))

    def test_str_of_digits_area(self):
        values = {
            (1.0001, 2.42): 1.210121,
            (1987329.123056, 5987129378.123978123): 5.9491983e+15,
            (4, 5): 10,
            (10000000000000000000, 4): 20000000000000000000,
            (-1, 123987): None,
            (-0.0000000000000000000001, 0): None,
            (142389923.12312, -1123987132987): None
        }
        for v in values:
            self.assertEqual(triangle.area(*v), values[v])

    def test_some_str_area(self):
        values = [
            ('asd', 1),
            (2, '2a'),
            ('sad1', 'iuy'),
            ('', 234),
        ]
        for v in values:
            self.assertIsNone(triangle.area(*v))

    def test_zero_perimeter(self):
        # values must be positive
        values = {
            (0, 0, 0): 0,
            (0, 1, 1): 2,
            (40, 0, 40): 80,
            (40, 12, 0): None  # triangle can't exist
        }
        for v in values:
            self.assertIsNone(triangle.perimeter(*v))

    def test_positive_perimeter(self):
        values = {
            (1, 1, 1): 3,
            (3, 4, 7): 17,
            (10, 20, 31): None,  # triangle can't exist
        }
        for v in values:
            self.assertEqual(triangle.perimeter(*v), values[v])

    def test_float_perimeter(self):
        values = {
            (1.00000, 123.123, 123.456): 247.579,
            (65.333, 55.987, 71.4849201): 192.8049201,
            (10 ** (-100), 10 ** (-100), 10 ** (-100)): 3 * 10 ** (-100)
        }
        for v in values:
            self.assertAlmostEqual(triangle.perimeter(*v), values[v])

    def test_negative_perimeter(self):
        values = [
            (-1, 123, 123),
            (1, -10 ** (-100), 1),
            (400, 985, -999.999),
            (-1, 0, -1)
        ]
        for v in values:
            self.assertIsNone(triangle.perimeter(*v))

    def test_str_of_digits_perimeter(self):
        values = {
            ('65.333', '55.987', '71.4849201'): 192.8049201,
            ('3', '4', '7'): 17,
            ('-1', '0', '-1'): None,
            ('400', '985', '-999.999'): None,
            '-123.2': None,
        }
        for v in values:
            self.assertEqual(triangle.perimeter(*v), values[v])

    def test_some_str_perimeter(self):
        values = [
            ('asd', 1, 1),
            (2, '2a', 1),
            ('sad1', 'iuy'),
            ('', 234, 250),
        ]
        for v in values:
            self.assertIsNone(triangle.perimeter(*v))


if __name__ == '__main__':
    unittest.main()
