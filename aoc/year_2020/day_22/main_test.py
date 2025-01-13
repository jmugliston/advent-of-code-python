import unittest
import os
from . import part1, part2


class TestMain(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, "input/example.txt"), "r") as file:
            self.data = file.read()

    def test_part1_example(self):
        self.assertEqual(part1(self.data), 306)

    def test_part2_example(self):
        self.assertEqual(part2(self.data), 291)


if __name__ == "__main__":
    unittest.main()
