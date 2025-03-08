# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 字符串转换为字典
str1= "k:1 |k1:2|k2:3|k3:4"
d = {k : int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
print(d)