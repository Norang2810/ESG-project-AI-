# 소괄호 () 로 작성
# 추가 수정 삭제 불가능
# 순서가 있는집합 (리스트와 동일)

tuple1 = (0,1,2,3,('a','b','c'),5)


# 2출력

print(tuple1[2])

# 1,2출력

print(tuple1[1:3])

# 3부터 끝까지

print(tuple1[3:])

print(len(tuple1))


# 리스트 튜플 공통점 ,차이점
# -공통점
# 요소를 가지고있음
# 요소순서 (인덱스 가지고있음)

# -차이점
# 리스트는 가변적
# 튜플은 불변적적


# ---------------------------
# in , not in

# in: 찾고자 하는 값이 포함되어 있으면 True
# not in : 찾고자 하는 값이 포함되어 있지 않으면 True




student = ['가','나','다','라']

if '가' in student:
    print('학생이 존재')
else :
    print('학생이 존재X')



if '가' not in student:
    print('학생이 존재')
else :
    print('학생이 존재X')

