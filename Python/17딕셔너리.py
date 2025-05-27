# 단어 그대로 사전이라는 뜻
# dictionary = key 와 Value 를 한쌍으로 갖는 자료형
# immutable한 key와 mutable한 Value

# 딕셔너리명 = {Key : Value,Key : Value, ＊＊＊}

#%%
# 딕셔너리 생성
# 중괄호 사용
# key : value를 한쌍으로 입력
dic1 ={"name":"MH","age":"20","phone":"010-7732-7280"}
print(dic1)
dic1['birth'] = '03/27'

# %%
dic_test = {'노래제목' : '아무노래'}
print(dic_test)
# %%
dic_test ['가수'] = '지코'
dic_test ['날짜'] = '2020.01.13'
print(dic_test)
# %%
# del 딕셔너리명 [Key]  삭제 
dic3 ={"name":"MH","age":"20","phone":"010-7732-7280"}
del dic3['name']
print(dic3)
# %%
dic3.clear()
print(dic3)
# %%
# key값을 통해서 인덱스
# value값이 출력
print(dic_test['가수'])

# %%
# 딕셔너리 값 가져오기 get(key)함수
print(dic_test.get('가수'))

# %%
list(dic_test.keys())
# %%
dic_test.values()
# %%
