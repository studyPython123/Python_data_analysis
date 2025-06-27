# Author: 邵世昌
# CreateTime: 2025/3/31
# FileName: 17__mro__
class  A:
    def test(self):
        print("Atest方法")
    def demo(self):
        print("Ademo方法")


class B:
    def demo(self):
        print("Bdemo方法")
    def test(self):
        print("Btest方法")

class C(A,B):
    pass
c = C()
c.test()
c.demo()
print(C.__mro__) # 查看底层逻辑 ，方法搜索顺序