import csv
import os

# CSVファイルのパスを指定する
csv_file_path = "原神キャラ一覧.csv"

# フォルダを作成する関数を定義する


def create_folder(path):
    try:
        os.makedirs(path)
        print("フォルダを作成しました: {}".format(path))
    except FileExistsError:
        print("フォルダはすでに存在します: {}".format(path))


# CSVファイルを読み込み、フォルダを作成する
with open(csv_file_path, "r",encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        folder_path = row[0]  # CSVファイルの1列目にフォルダのパスが入っていると仮定する
        create_folder(folder_path)
