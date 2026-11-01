import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_singleton(self):
        self.assertIs(Calculator(), Calculator())

    def test_numeric_strings(self):
        self.assertEqual(self.calc.add("1", "1"), 2)
        self.assertAlmostEqual(self.calc.add("1", "1.600"), 2.6)

    def test_languages(self):
        examples = [
            ("three", "four", 7),
            ("fünf", "sechs", 11),
            ("cinco", "siete", 12),
            ("семь", "восемь", 15),
            ("三", "五", 8),
            ("III", " VIII ", 11),
            ("0", "X", 10),
        ]
        for first, second, expected in examples:
            with self.subTest(first=first, second=second):
                self.assertEqual(self.calc.add(first, second), expected)

    def test_other_operations(self):
        self.assertEqual(self.calc.sub(3, 4), -1)
        self.assertEqual(self.calc.mul("ocho", "nueve"), 72)
        self.assertEqual(self.calc.div("ocho", "dos"), 4)

    def test_prime_factors(self):
        examples = [
            (1, []),
            (27, [3, 3, 3]),
            (1092, [2, 2, 3, 7, 13]),
            (32768, [2] * 15),
            (10952347, [7, 23, 59, 1153]),
        ]
        for number, expected in examples:
            with self.subTest(number=number):
                self.assertEqual(self.calc.factorize(number), expected)

    def test_invalid_factorization(self):
        for number in (0, -5, 2.5):
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    self.calc.factorize(number)

    def test_unknown_word(self):
        with self.assertRaises(ValueError):
            self.calc.add("banana", 1)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)
