#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

string = '''
    abcd
    abcd
'''

# 相当于
# 1. 编译正则表达式
# (.*)      贪婪匹配，尽可能多匹配直到无法匹配
# (.*?)     非贪婪匹配，只要匹配到就返回
#  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
# re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
pattern = re.compile(r'a(.*)d', re.RegexFlag.S)

# 2. 提取数据
result = pattern.findall(string)
print(result)
pattern = re.compile(r'a(.*?)d', re.RegexFlag.S)

# 2. 提取数据
result = pattern.findall(string)
print(result)