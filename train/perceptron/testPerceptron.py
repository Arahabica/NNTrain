# -*- coding: utf-8 -*-
import unittest
from Perceptron import Perceptron


class TestPerceptron(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.perceptron = Perceptron()

    def test_AND(self):
        self.assertEqual(0, self.perceptron.AND(0, 0))
        self.assertEqual(0, self.perceptron.AND(0, 1))
        self.assertEqual(0, self.perceptron.AND(1, 0))
        self.assertEqual(1, self.perceptron.AND(1, 1))

    def test_NAND(self):
        self.assertEqual(1, self.perceptron.NAND(0, 0))
        self.assertEqual(1, self.perceptron.NAND(0, 1))
        self.assertEqual(1, self.perceptron.NAND(1, 0))
        self.assertEqual(0, self.perceptron.NAND(1, 1))

    def test_OR(self):
        self.assertEqual(0, self.perceptron.OR(0, 0))
        self.assertEqual(1, self.perceptron.OR(0, 1))
        self.assertEqual(1, self.perceptron.OR(1, 0))
        self.assertEqual(1, self.perceptron.OR(1, 1))

    def test_XOR(self):
        self.assertEqual(0, self.perceptron.XOR(0, 0))
        self.assertEqual(1, self.perceptron.XOR(0, 1))
        self.assertEqual(1, self.perceptron.XOR(1, 0))
        self.assertEqual(0, self.perceptron.XOR(1, 1))

if __name__ == '__main__':
    unittest.main()