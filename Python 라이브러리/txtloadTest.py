# %%
f = open('data.txt','r')
print(f)
# %%
data = f.read()
print(data)
# %%
print(type(data))
# %%
# 파일 읽기
with open('data.txt', 'r') as f:
    data = f.read()
    print(data)
with open('data.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('This is a test file.\n')
# %%