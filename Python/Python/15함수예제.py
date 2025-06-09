#%%
def cal(num1,num2,op):
    if op =="+":
     return num1 + num2
    else:
        return num1 - num2

# %%
num1 = int(input('첫번째 점수를 입력>>'))
num2 = int(input('두번째 점수를 입력>>'))
op = input('연사자 입력(+,-)>>')

result = cal(num1,num2,op)
print('결과 : {}'.format(result))

# %%
# DocString (Shift + Tab)