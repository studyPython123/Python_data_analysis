# Author: 邵世昌
# CreateTime: 2024/12/1
# FileName: 汉诺塔问题
def hannuota(n,a,b,c): #表示将n个圆盘从a移动到c
    if n > 0 :
        # 将n-1个圆盘的移动看作是一个子问题，分三步走
        hannuota(n-1,a,c,b)
        print("moving form %s to %s" % (a,c))
        hannuota(n-1,b,a,c)
# 运行函数
if __name__ == '__main__':
    hannuota(3, "A", "B", "C")
