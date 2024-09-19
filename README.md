# GitHub Repository Trends by Language

このプロジェクトは、GitHub APIを使用して指定されたプログラミング言語に関するリポジトリのデータを取得し、そのデータをCSVファイルに保存し、言語ごとのスター数を可視化するスクリプトです。

## 機能

1. **データ取得**: 指定されたプログラミング言語のGitHubリポジトリ情報を取得し、CSVファイルに保存します。
2. **データ可視化**: CSVファイルからデータを読み込み、各プログラミング言語のリポジトリにおけるスター数を棒グラフで可視化します。

## 使い方

1. **必要なライブラリのインストール**

   ```bash
   pip install requests pandas matplotlib
   ```

2. **スクリプトの実行**

   スクリプトを実行することで、指定された言語のGitHubリポジトリデータを取得し、`github_trends_multi_lang.csv`という名前のCSVファイルに保存します。その後、CSVファイルのデータを用いて各言語のスター数を棒グラフとして表示します。

   ```bash
   python github_language_trends.py
   ```

## スクリプトの詳細

- **`fetch_github_data(languages)`**: GitHub APIを使用してリポジトリデータを取得し、CSVファイルに保存します。`languages`パラメータには、分析したいプログラミング言語のリストを指定します。

- **`visualize_data()`**: 保存されたCSVファイルからデータを読み込み、言語ごとのスター数を棒グラフで可視化します。

## CSVファイルのフォーマット

- `name`: リポジトリ名
- `language`: プログラミング言語
- `stars`: スター数
- `forks`: フォーク数
- `created_at`: 作成日

## デモ

以下の図は、各プログラミング言語のリポジトリのスター数を示した棒グラフです。

![Figure_1](https://github.com/user-attachments/assets/eca258d8-9a16-4078-8f06-c1856232446c)

## 注意事項

- GitHub APIのリクエスト制限に達した場合、データ取得が失敗する可能性があります。
- 大量のデータを取得する場合、APIの制限により複数回のリクエストが必要になることがあります。
