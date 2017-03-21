# -*- coding: utf-8 -*-
import unittest
import numpy as np
import matplotlib.pyplot as plt
from NeuralTrain import NeuralTrain


class TestNeuralTrain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.neural = NeuralTrain()

    def test_step_function(self):
        y = self.neural.step_function(0.1)
        self.assertEqual(1, y)
        y = self.neural.step_function(-0.1)
        self.assertEqual(0, y)
        y = self.neural.step_function(np.array([-1, -0.1, 0.5, 6]))
        np.testing.assert_equal(np.array([0, 0, 1, 1]), y)
        ok = True
        try:
            # 普通の配列は受け付けない
            y = self.neural.step_function([-1, -0.1, 0.5, 6])
        except Exception as e:
            ok = False
        self.assertFalse(ok)

    def test_sigmoid_function(self):
        y = self.neural.sigmoid_function(0)
        self.assertEqual(0.5, y)
        y = self.neural.sigmoid_function(100)
        self.assertAlmostEqual(1, y)
        y = self.neural.sigmoid_function(-100)
        self.assertAlmostEqual(0, y)
        y = self.neural.sigmoid_function(np.array([-1, -0.1, 0.5, 6]))
        np.testing.assert_array_almost_equal(np.array([0.26894142,  0.47502081,  0.62245933,  0.99752738]), y)
        ok = True
        try:
            # 普通の配列は受け付けない
            y = self.neural.step_function([-1, -0.1, 0.5, 6])
        except Exception as e:
            ok = False
        self.assertFalse(ok)

    def show_graph(self, p, title, func):
        x = np.arange(-5.0, 5.0, 0.1)
        y = func(x)
        p.set_title(title)
        p.plot(x, y)
        # p.ylim(-0.1, 1.1)
        return p

    def test_step_show(self):
        fig, (p1, p2, p3) = plt.subplots(ncols=3, figsize=(20, 4))
        self.show_graph(p1, 'Step Function', self.neural.step_function)
        self.show_graph(p2, 'Sigmoid Function', self.neural.sigmoid_function)
        self.show_graph(p3, 'ReLU Function', self.neural.relu_function)
        plt.ylim(-0.1, 1.1)
        plt.show()

if __name__ == '__main__':
    unittest.main()
