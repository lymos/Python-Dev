#!/usr/bin/python3

# 处理xml数据
# 1. xml.sax  2. dom

import xml.sax

'''
 1. xml.sax
'''
class xmlHandle(xml.sax.ContentHandler):    # 继承 ContentHandler 对象

    def __init__(self): # 构造函数
        self.CurrentData = ""

    # 元素开始时调用这个函数
    def startElement(self, tag, attributes):
        print("start element")

    # 元素结束时调用这个函数
    def endElement(self, tag):
        print("end element")

    # 读取元素时调用
    def characters(self, content):
        print(content)

'''
    在cmd 中直接运行.py文件,则__name__的值是'__main__';
    而在import 一个.py文件后,__name__的值就不是'__main__'了;
    从而用if __name__ == '__main__'来判断是否是在直接运行该.py文件
'''
if(__name__ == "__main__"):
    # 创建一个XMLReader
    xml_parser = xml.sax.make_parser()
    # 重写ContentHandler
    my_handle = xmlHandle()
    xml_parser.setContentHandler(my_handle)
    # trun off namespace
    xml_parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    data = """<?xml version="1.0" encoding="UTF-8"?>
        <note><to>World</to><from>Linvo</from><heading>Hi</heading>
        <body>Hello World!</body></note>"""
   # xml_parser.parseString(data, my_handle) # 解析字符串
   # xml_parser.parse(file) # 解析文件


'''
 2. dom
'''
class myDom:
    def __init__(self):
        print("init")

    # 待续...

myDom = myDom()