# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt, mpld3
from matplotlib.image import imread
import os

# mpld3: matplotによる描画をjs(D3.js)に変換
# http://mpld3.github.io/


def simple():
    """ y = sin(x) の図の表示 """
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


def sin_cos_plt():
    """
    y = sin(x)
    y = cos(x)
    の2つの図の表示するmatplotオブジェクトを作成
    :return:
    """
    x = np.arange(0, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle="--", label="cos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("sin & cos")
    plt.legend()
    return plt


def sin_cos_show():
    """
    matplotlibの標準表示画面でy=sin(x), y=cos(x)の図の表示
    :return:
    """
    plt = sin_cos_plt()
    plt.show()


def sin_cos_d3():
    """
    Web上でy=sin(x), y=cos(x)の図の表示
    :return:
    """
    plt = sin_cos_plt()
    mpld3.show(plt.gcf())


def sin_cos_d3_save():
    """
    Web上でy=sin(x), y=cos(x)の図の表示するためのデータをJSONで保存
    :return:
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(base, 'result/sin_cos.json'))
    plt = sin_cos_plt()
    mpld3.save_json(plt.gcf(), open(path, "w"))


def show_image():
    base = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.normpath(os.path.join(base, 'lena.png'))
    img = imread(image_path)
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    #simple()
    sin_cos_show()
    #sin_cos_d3()
    #sin_cos_d3_save()
    #show_image()