#!/usr/bin/python3

# python 操作json
import json # 导入json库

data = {
    "name": "admin",
    "date": "2016-04-12"
}  # 定义字典类型变量
json_str = json.dumps(data) # 转换成json
print("原始字典类型数据：", data)
print("JSON数据：", data)

# json 转换成字典
dict_data = json.loads(json_str)
print("\n")
print("JSON转换成字典：")
print("data['name'] = ", dict_data['name'])

'''
    处理含有JSON数据的文件
    写入
    with open("json.json", "w") as file:
        json.dump(data, file)
    读取
    with open("json.json", "r") as file:
        data json.load(file)

'''