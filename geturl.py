from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import os
import shutil
import urllib.request
import zipfile

model_dir = './model'
# モデルディレクトリを削除
# shutil.rmtree(model_dir)

with open('url.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[0]
        version = row[1]
        # バージョンディレクトリを作成
        version_dir = os.path.join(model_dir, version)
        os.makedirs(version_dir, exist_ok=True)
        names = row[2:]
        for name in names:
            print(name)
            # name_dir = os.path.join(version_dir, name)
            # os.makedirs(name_dir, exist_ok=True)
        
        # ブラウザを開く
        driver = webdriver.Chrome()
        driver.maximize_window()
        # URLにアクセス

        driver.get(url)
        # ページが完全に読み込まれるまで待つ
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located)
        print(f"onload: {url}")
        # time.sleep(2)

        elements = driver.find_elements(By.XPATH, "//*[@href]")
        urls = set()

        for element in elements:
            href = element.get_attribute("href")
            if href.endswith('.zip') or href.endswith('.rar'):
                if href not in urls:
                    print(href)
                    with open(f'{version_dir}/output.csv', 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow([href])
                    urls.add(href)

        urls.clear()
        # ブラウザを閉じる
        driver.quit()
        
for href in urls:
    # ファイルをダウンロード
    file_name = href.split('/')[-1]
    urllib.request.urlretrieve(href, os.path.join(version_dir, file_name))

# model_dir がモデルディレクトリへのパスであると仮定します
# モデルディレクトリ内のファイルを走査し、zip または rar ファイルを見つけたら解凍します
for root, dirs, files in os.walk(model_dir):
    for file in files:
        if file.endswith(".zip") or file.endswith(".rar"):
            file_path = os.path.join(root, file)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # ファイル名のエンコード方式を考慮して解凍
                for file_info in zip_ref.infolist():
                    try:
                        file_info.filename = file_info.filename.encode('cp437').decode('gb18030')
                    except Exception as e:
                        file_info.filename = file_info.filename.encode('utf-8').decode('utf-8')
                    zip_ref.extract(file_info, root)