#%%
##  예외처리
try:
        '가' + 10
except:
        print('오류입니다.')
# %%
# open("파일명","모드") :파일을 연다.

f = open('test.txt','w')
# close() :파일 닫기 
f.close()
# %%

f = open("test.txt",'w')
f.write('Hello\nPython is Fun.')
f.close()
# %%
f =open ('test.txt','r')
line = f.readline() #파일에 있는 내용 한줄 읽기
print(line)
f.close()
# %%
# 전체파일내용 읽기
try :
    f = open('test.txt','r')

    while True:
        line = f.readline()
        if not line:
         break
    print(line)
    
    f.close()
except:
    print('파일읽기를 실패했습니다.')
    
# %%
f = open('test.txt','r')
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()
# %%
f = open('test.txt','a')
f.write('\n Python is easy')
f.close()
# %%
with open('test.txt','w') as f:
    f.write('안녕하세요\nPython입니다.')
# %%
import os
dirname = 'C:\Dev\ESG\Python'

filenames = os.listdir(dirname)
filenames
for filename in filenames:
    full_filename = os.path.join(dirname)
    print(full_filename)    
# %%
import os
if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('파일이 존재하지않습니다.')
# %%
import os
DIR = './test/'

if not os.path.exists(DIR):
    os.rmdir(DIR)
else :
    print('폴더가 존재하지않습니다.')