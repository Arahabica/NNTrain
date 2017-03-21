[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
# 概要
[ゼロから作るDeep Learning](https://www.oreilly.co.jp/books/9784873117584/) の学習

![zerodeep](https://cloud.githubusercontent.com/assets/1854729/24141366/904c5cc8-0e66-11e7-8fd9-a6a968828728.jpg)

# Tips
1. Python 3.5.0からは行列の内積に`@`が使える
```
matrix = matrixA.dot(matrixB)  # 今まで
matrix = matrixA @ matrixB   # python3.5以降
```

2. matplotlibをD3(javascript)で描画

* /train/matplotlib/matplotlib_train.py 参照
```
import matplotlib.pyplot as plt, mpld3

x = np.arange(0, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
# plt.show()  # 通常のmatplotlibのグラフ表示
mpld3.show(plt.gcf())  # D3で描画
# mpld3.save_json(plt.gcf(), open("./graph.json", "w"))  # D3で描画するためのjsonを出力
```
# Setup
1. pyenv と pyenv-virtualenv をインストール
2. 下記コマンドを実行

```cmd
$ bash ./setup.sh
```

3. テスト

```cmd
$ bash ./test.sh
```