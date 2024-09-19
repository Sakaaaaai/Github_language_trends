import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

# GitHubデータを取得してCSVに保存する関数
def fetch_github_data(languages):
    url = "https://api.github.com/search/repositories"
    all_repos = []

    for language in languages:
        params = {
            'q': f'language:{language}',
            'sort': 'stars',
            'order': 'desc',
            'per_page': 2000
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        for repo in data['items']:
            all_repos.append({
                'name': repo['name'],
                'language': repo['language'],
                'stars': repo['stargazers_count'],
                'forks': repo['forks_count'],
                'created_at': repo['created_at']
            })
    
    with open('github_trends_multi_lang.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'language', 'stars', 'forks', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_repos)

    print("Data fetching and saving completed.")

# GitHubリポジトリの言語ごとのスター数を可視化する関数
def visualize_data():
    # CSVデータの読み込み
    df = pd.read_csv('github_trends_multi_lang.csv')

    # 言語ごとのスター数を集計
    df_grouped = df.groupby('language')['stars'].sum().reset_index()
    df_grouped.sort_values(by='stars', ascending=False, inplace=True)

    # 色のリストを定義（言語の数に応じて調整）
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgoldenrodyellow', 'lightsteelblue']
    
    # データのプロット
    plt.figure(figsize=(12, 8))
    bars = plt.bar(df_grouped['language'], df_grouped['stars'], color=colors[:len(df_grouped)])
    plt.title('GitHub Repository Stars by Language')
    plt.ylabel('Number of Stars')
    plt.xlabel('Programming Language')
    plt.xticks(rotation=45)
    
    # グラフに凡例を追加
    plt.legend(bars, df_grouped['language'], title='Programming Language', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()

# メイン処理
if __name__ == "__main__":
    languages = ['python', 'javascript', 'java', 'ruby', 'go', 'c']
    fetch_github_data(languages)
    visualize_data()
