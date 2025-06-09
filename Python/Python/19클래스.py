# 클래스는 객체의 구조(변수,속성)를 포함하고있는 자료형

# 인스턴스 : 클래스 객체를 가리키는 변수

#   class 클래스명:
#        클래스 변수
    
#        def 클래스 함수(self,인자1,인자2...):
#             실행문

#%%
class SampleClass:
    def setname(self,name):
        self.name = name
        
    def sum(self,a,b):
        result = a+b
        print("%s님 %d+%d=%d입니다" %(self.name,a,b,result))
    
    def hap(self,a,b):
        return a+b        
# %%
a = SampleClass()
a.setname("홍길동")
a.sum(10,20)
# %%
print(a.hap(10,20))
#
# %%
# self : 현재클래스를 받은 인스턴스를 가르키는 변수
# 클래스 호출시에 클래스로 호출한 객체 자신이 전달됨

    # -접근자 함수 사용하기기
    # >허가된 객체만 접근하게 하기 위한것
    