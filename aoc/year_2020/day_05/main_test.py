import unittest
import os
from . import part1, part2


class TestMain(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, "input/example.txt"), "r") as file:
            self.data = file.read()
        with open(os.path.join(dir, "input/input.txt"), "r") as file:
            self.input = file.read()

    def test_part1_example(self):
        self.assertEqual(part1(self.data), 820)

    def test_part2_example(self):
        self.assertEqual(part2(self.input), 617)


if __name__ == "__main__":
    unittest.main()