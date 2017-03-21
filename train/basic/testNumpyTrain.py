# -*- coding: utf-8 -*-
import unittest
import numpy as np


class TestNumpyTrain(unittest.TestCase):
    """ Numpy の練習 """
    @classmethod
    def setUpClass(cls):
        pass

    def test_basic_calc_array(self):
        """ 配列の四則演算 """
        x = np.array([1.0, 2.0, 3.0])
        y = np.array([2.0, 4.0, 6.0])
        # 足し算
        np.testing.assert_equal(np.array([3.0, 6.0, 9.0]), x + y)
        # 引き算
        np.testing.assert_equal(np.array([-1.0, -2.0, -3.0]), x - y)
        # 掛け算
        np.testing.assert_equal(np.array([2.0, 8.0, 18.0]), x * y)
        # 割り算
        np.testing.assert_equal(np.array([0.5, 0.5, 0.5]), x / y)

    def test_basic_calc_matrix(self):
        """ 行列の四則演算 """
        x = np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0]])
        y = np.array([[1.0, 3.0, 5.0], [1.0, 2.0, 7.0]])
        # 足し算
        np.testing.assert_equal(np.array([[2.0, 5.0, 8.0], [3.0, 6.0, 13.0]]), x + y)
        # 引き算
        np.testing.assert_equal(np.array([[0.0, -1.0, -2.0], [1.0, 2.0, -1.0]]), x - y)
        # 掛け算
        np.testing.assert_equal(np.array([[1.0, 6.0, 15.0], [2.0, 8.0, 42.0]]), x * y)
        # 割り算
        np.testing.assert_equal(np.array([[1.0, 2.0 / 3.0, 3.0 / 5.0], [2.0, 2.0, 6.0 / 7.0]]), x / y)

    def test_broadcast(self):
        """
        ブロードキャスト機能
        形状の異なる配列の演算も自動で保管して計算可能
        :return:
        """
        x = np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0]])
        np.testing.assert_equal(x * np.array([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]), x * 2.0)
        np.testing.assert_equal(x * np.array([[3.0, 2.0, 1.0], [3.0, 2.0, 1.0]]), x * np.array([3.0, 2.0, 1.0]))

if __name__ == '__main__':
    unittest.main()