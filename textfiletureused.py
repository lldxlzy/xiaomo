#! /user/bin python 3.8.0
#! /git.lingmo/xiaomo cheak file
import requests
import zipfile
import os
import hashlib

def download_file(url, destination):
    # 下载文件
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
    else:
        print("下载失败，状态码：", response.status_code)

def unzip_file(zip_path, extract_to):
    # 解压文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def calculate_sha256(file_path):
    # 计算文件的 SHA-256 哈希值
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

# 示例用法
url = 'http://example.com/yourfile.zip'  # 替换为实际文件 URL
destination = 'yourfile.zip'
extract_to = 'extracted_files'
expected_sha256 = 'expected_sha256_hash_here'  # 替换为期望的 SHA-256 哈希值

# 步骤 1：下载文件
download_file(url, destination)

# 步骤 2：解压文件
unzip_file(destination, extract_to)

# 步骤 3：检查文件的一致性
downloaded_sha256 = calculate_sha256(destination)
if downloaded_sha256 == expected_sha256:
    print("文件一致性检查通过！")
else:
    print("文件一致性检查失败！")

# 可选：删除下载的 ZIP 文件
os.remove(destination)