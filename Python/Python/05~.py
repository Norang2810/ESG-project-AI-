num = int(input("정수 입력 >> "))

result = "홀수" if num % 2 == 1 else "짝수"

print("{}는(은) {}입니다.".format(num,result))