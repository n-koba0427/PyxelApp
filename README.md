# PyxelApp

[`PyxelApp`](https://pypi.org/project/pyxel-app/)はPyxelのアプリケーションテンプレートを簡単に作成するbashコマンドを提供します。

## 目次

- [インストール](#インストール)
- [使い方](#使い方)
- [機能](#機能)
- [フィードバックと貢献](#フィードバックと貢献)
- [ライセンス](#ライセンス)

## インストール

```
pip install pyxel_app
```

## 使い方

1. コマンドラインを開きます。
2. 次のコマンドを入力します：

```
pyxel_app [プロダクト名]
```

例:

```
pyxel_app my_new_game
```

これにより、`my_new_game`という名前のpyxelアプリケーションテンプレートが現在のディレクトリに作成されます。

### ディレクトリ構造

```
my_new_game
├── entry.py
└── pkg
    ├── __init__.py
    ├── app.py
    ├── data
    │   └── img.pyxres
    └── utils.py
```

### 実行方法

テンプレートを作成した後、以下のコマンドを実行することで、Pyxelアプリケーションを起動することができます。

/```
python my_new_game/entry.py
/```

このコマンドにより、`entry.py`が実行され、Pyxelアプリケーションが起動します。


## 機能

- Pyxelの基本的なテンプレートをすばやく自動生成
- ユーザー指定のプロダクト名を基にしたディレクトリ構造の生成

## フィードバックと貢献

プロジェクトへのフィードバックや貢献をお待ちしております。詳細はGitHubリポジトリをご参照ください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、同梱の`LICENSE`ファイルを参照してください。
