import zipfile
import os
import chardet
from chardet.universaldetector import UniversalDetector
import shutil
import subprocess


def unzip_all_files(folder_path):
    # フォルダ内のファイルとサブフォルダを再帰的に探索
    for i, (root, dirs, files) in enumerate(os.walk(folder_path)):
        for file in files:

            # zipファイルであれば解凍
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                # 解凍するフォルダ名を親フォルダの連番にする
                folder_name = f"{os.path.basename(root)}_{os.path.splitext(file)[0]}_{i}"
                folder_path = os.path.join(root, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                # zipファイルを解凍してフォルダに保存
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    for file_info in zip_ref.infolist():
                        # ファイル名をUTF-8にエンコードして解凍する
                        print('test',folder_name)
                        try:
                            file_info.filename = file_info.filename.encode('cp437').decode('gb18030')
                        except Exception as e:
                            print(e)
                            file_info.filename = file_info.filename.encode('utf-8').decode('utf-8')
                        zip_ref.extract(file_info, folder_path)
                        print(f'{folder_path}/{file_info.filename}')
                        #code(f'{folder_path}/{file_info.filename}')
                        print(f"Extracted {file_path} to {folder_path}\n")
                # os.remove(file_path)
                # print(f"Removed {file_path}")


def code(file):
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        result = detector.result
        print(result)


# 使用例
unzip_all_files("./原神 - コピー")

# 迪卢克
# 使用规则
# readme亂堦掕梫娕亃