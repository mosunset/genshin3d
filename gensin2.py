import os
import shutil
import rarfile
import zipfile

# RARファイルをZIPファイルに変換する関数
def convert_to_zip(file_path):
    with rarfile.RarFile(file_path) as rf:
        # 出力ファイル名を決定
        zip_path = os.path.splitext(file_path)[0] + '.zip'
        # ZIPファイルを作成し、RARファイルの内容をコピー
        with zipfile.ZipFile(zip_path, 'w',encoding='UTF-8') as zf:
            for name in rf.namelist():
                data = rf.read(name)
                zf.writestr(name, data)

# 指定されたディレクトリ以下のすべてのRARファイルを検索し、それらをZIPファイルに変換する関数
def convert_dir_to_zip(dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # RARファイルを検索
            if filename.endswith('.rar'):
                file_path = os.path.join(dirpath, filename)
                # RARファイルをZIPファイルに変換
                convert_to_zip(file_path)

# ディレクトリのパスを指定して、RARファイルをZIPファイルに変換
convert_dir_to_zip('C:/Users/drive/Downloads/原神')
