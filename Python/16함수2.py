#%%
# * 가변매개변수 (튜플 형태)
def var_param(*args):
    print(args)

# %%
var_param(1,2,3)

# %%
var_param(1,2,3,4,5)
# %%
# ** 가변매개변수 (딕셔너리형태)
def print_map(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,"|",value)
# %%
print_map(하나 =1)
# %%
# 매개변수 기본값 설정 가능능
def cal(n1,n2,op="+"):
    if op == "+":
        return n1+n2
    else :
        return n1-n2
cal(10,20)
# %%
def power_of_N(num,power =2):
    return num ** power
# %%
power_of_N(3,2)
# %%
def add_sub (n1,n2):
    return n1+n2,n1-n2
# %%
add_sub(10,7)