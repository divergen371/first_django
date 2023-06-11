# Django入門

## プロジェクトを作る

- プロジェクト
  - Webアプリのこと
- アプリ
  - Webアプリの個別機能のこと

- `django-admin startproject create .`でプロジェクトを始める。
  - ディレクトリ名は任意だが、慣習的にconfigとすることが多い。
- `python manage.py runserver`でサーバーの立ち上げ。
- `python manage.py startapp <app名>`でアプリを準備する。
- 使用する言語やタイムゾーン、その他各種設定はプロジェクト直下のsetting.pyを編集する。
- 作成したアプリもsetting.pyに登録する。

## モデルを作る

- `python manage.py migrate`でデフォルト機能のテーブルをデータベースに反映させる。
  - アプリのテーブルが設計できているなら、そのモデルを書いてマイグレーションファイルを生成してから纏めて実行する。
- マイグレーションファイルの生成は`python manage.py makemigrations`。
- 先にも書いたが、マイグレーションファイルのテーブルへの登録は`python manage.py migrate`。

## 管理者を作成する

- `python manage.py createsuperuser`で対話が始まるので従っていく
- アプリディレクトリ直下の`admin.py`にモデルを登録すると管理画面で操作できるようになる。

## Djangoの仕組み

### MVT

- MVT(model-view-template)という考え方に基づいて設計されている。
- URLにアクセスするとViewが機能しモデルやテンプレートを呼び出す。
- モデルは`models.py`
  - データベース連携
- Viewは`Views.py`、`urls.py`
  - `views`はロジック、`urls`はルーティング
  - `views`テンプレートの呼び出し、モデルの呼び出し
- テンプレートは`<アプリディレクトリ>/templates/*`
