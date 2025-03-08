# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 生成随机验证码
import  random
def generate_code(code_len):
    code_all = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(code_len):
        index = random.randint(0,len(code_all)-1)
        code += code_all[index]
    return code
code_len = eval(input("验证码的长度为：len = "))
print(generate_code(code_len))