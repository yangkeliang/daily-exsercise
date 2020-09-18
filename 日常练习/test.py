# import os
# os.getcwd()
# print(os.listdir(path="."))
# os.mkdir("ykl")
# os.system("calcf")

# print('''hello
# hello''')
# # help(print)

# def ceishi():
#     '''可亮，坚持下去啊'''
#     print("加油")

# if __name__=="__main__":
#     ceishi()
#     help(ceishi)

import re

if (__name__=="__main__"):
    r=re.compile(r"\d{1,3}")
    print(r.match("22").group(0))