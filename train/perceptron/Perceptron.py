# -*- coding: utf-8 -*-
# 2章 パーセプトロン
import numpy as np


class Perceptron:
    """
    パーセプトロン
    単層パーセプトロンでは線形的な問題しか解くことができない。
    線形的な問題: グラフ上の点を直線によって分ける問題
    """
    def AND(self, x1, x2):
        """
        ANDゲート
        :param float x1: 入力1
        :param float x2: 入力2
        :return: int
        """
        x = np.array([x1, x2])    # 入力信号
        w = np.array([0.5, 0.5])  # 重み
        b = -0.7                  # バイアス
        res = np.sum(w * x) + b
        if res <= 0:
           return 0
        else:
           return 1

    def NAND(self, x1, x2):
        """
        NANDゲート
        ANDゲートのパラメータを変えただけだが、汎用化されたnodeメソッドをしようしている。
        :param float x1: 入力1
        :param float x2: 入力2
        :return: int
        """
        return self.node(np.array([x1, x2]), np.array([-0.5, -0.5]), 0.8)

    def OR(self, x1, x2):
        """
        ORゲート
        ANDゲートのパラメータを変えただけだが、汎用化されたnodeメソッドをしようしている。
        :param float x1: 入力1
        :param float x2: 入力2
        :return: int
        """
        return self.node(np.array([x1, x2]), np.array([0.5, 0.5]), -0.4)

    def XOR(self, x1, x2):
        """
        XORは単層パーセプトロンでは解けない。多層パーセプトロンが必要
        :param float x1:
        :param float x2:
        :return: int
        """
        y1 = self.NAND(x1, x2)
        y2 = self.OR(x1, x2)
        return self.AND(y1, y2)

    def node(self, x, w, b):
        return np.int(np.sum(w * x) + b > 0)
