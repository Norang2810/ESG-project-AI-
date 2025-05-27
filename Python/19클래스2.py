# %%
class SampleClass:

    __var = 200

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %d+%d=%d입니다." % (self.name, a, b, result))

    def setVar(self, var):
        self.__var = var

    def getVar(self):
        return self.__var


# %%
a = SampleClass("홍길동")  # 생성자
# %%
a.sum(10, 20)
# %%
# print(a.__var)      #__접근은 일반적으로 불가
# %%
# __클래스 변수는 : setter(),getter() 메소드로 활용

a.setVar(400)
print(a.getVar())
# %%

# 계산기


class CalClass:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2


# %%
a = CalClass(10, 20)
b = CalClass(30, 20)
# %%
print(a.add())
print(a.sub())
print(b.add())
print(b.sub())


# %%
# 파이썬은 다중상속이 가능한 언어
class SuperClass:
    def show(self):
        print("국가이름 : ", self.name)


class SubClass(SuperClass):
    def __init__(self, name):
        self.name = name
    def show(self):
        print("국가이름(Sub) : ",self.name)
        super().show()

# %%
a = SubClass("대한민국")
# %%
a.show()
# %%
# 연산자 오버로딩

class OperOverLoadClass:
    def __init__(self,var):
        self.var = var
        
    def __add__(self,other):
        print("%s %s"%(self.var,other.var))

# %%
a = OperOverLoadClass("Python")
b= OperOverLoadClass("is easy")
# %%
a+b
# %%
