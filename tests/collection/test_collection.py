import unittest
from src.collection import Collection


class TestCollection(unittest.TestCase):
    def setUp(self):
        self.c = Collection()

    def test_separate_objects(self):
        self.assertIsNot(Collection(), Collection())

    def test_contains(self):
        self.assertEqual(self.c.contains([1, 2, 1, 3], 1), 2)
        self.assertEqual(self.c.contains([1, 2], 9), 0)
        self.assertEqual(self.c.contains([], 1), 0)

    def test_zip(self):
        self.assertEqual(
            self.c.zip(["a", "b"], [1, 2]),
            [("a", 1), ("b", 2)],
        )

    def test_zip_unequal_and_empty(self):
        self.assertEqual(self.c.zip(["a", "b"], [1]), [("a", 1)])
        self.assertEqual(self.c.zip([], [1, 2]), [])

    def test_power_set(self):
        self.assertCountEqual(
            self.c.pset([1, 2, 3]),
            [(), (1,), (2,), (3,),
             (1, 2), (1, 3), (2, 3), (1, 2, 3)],
        )

    def test_power_set_empty_and_duplicates(self):
        self.assertEqual(self.c.pset([]), [()])
        self.assertCountEqual(
            self.c.pset([1, 1, 2]),
            [(), (1,), (2,), (1, 2)],
        )

    def test_permutations(self):
        self.assertCountEqual(
            self.c.perm([1, 2, 3]),
            [(1, 2, 3), (1, 3, 2), (2, 1, 3),
             (2, 3, 1), (3, 1, 2), (3, 2, 1)],
        )

    def test_permutations_empty_and_duplicates(self):
        self.assertEqual(self.c.perm([]), [()])
        self.assertCountEqual(
            self.c.perm([1, 1, 2]),
            [(1, 1, 2), (1, 2, 1), (2, 1, 1)],
        )
