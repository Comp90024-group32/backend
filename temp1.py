import json
from flask import Flask, jsonify
import couchdb
import requests
def f():
    with open("./data_twitter/marital_data(1).json", "r") as fa:
        content = fa.read()  # 读取文件内容
    data = json.loads(content)  # 解析 JSON 字符串
    result = set()
    for item in data:
        result.add(item['area'])
    print(result)

f()