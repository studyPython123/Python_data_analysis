# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 身体BMI质量检测
#%%
def function(weight, height):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        size = "偏瘦"
    elif BMI >= 18.5 and BMI < 24:
        size = "正常"
    elif BMI >= 24 and BMI < 28:
        size = "偏胖"
    else:
        size = "肥胖"
    print(f"您的BMI是{BMI:.2f}")
    print(size)
#%%
weight = float(input("请输入您的体重（kg）："))
height = float(input("请输入您的身高（m）："))
function(weight, height)
