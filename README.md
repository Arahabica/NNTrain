# 概要
[ゼロから作るDeep Learning](https://www.oreilly.co.jp/books/9784873117584/) の学習

![zerodeep](https://cloud.githubusercontent.com/assets/1854729/24141366/904c5cc8-0e66-11e7-8fd9-a6a968828728.jpg)

# Tips
Python 3.5.0からは行列の内積に`@`が使える
```
matrix = matrixA.dot(matrixB)  # 今まで
matrix = matrixA @ matrixB   # python3.5以降
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