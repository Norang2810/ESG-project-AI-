# %%
student = [] #name,num,python,r,stats
print('===================학점 관리 프로그램=======================')
while True:
    menu = int(input("[1]성적입력 [2]전체조회 [3]학생검색 [4]종료 :"))
    if menu ==4:
        print("종료되었습니다.")
        break
    elif menu==1:
        name = input("이름입력 : ")
        num = int(input("학번입력 : "))
        python = int(input("Python 점수입력 :"))
        r=int(input("R 점수입력 : "))
        stats=int(input("통계 점수입력 : "))
        # student리스트에 추가
        student.append([name,num,python,r,stats])
        print("-----------------------------------------------")
    elif menu==2:
        print("==================전체조회====================")
        print('이름\t학번\tPython\tR\t통계\t평균\t학점')
        for info in student:
            mean = (info[2]+info[3]+info[4]) /3
            grade = ""
            if mean >=90:
                grade ='A'
            elif mean>=80:
                grade ='B'
            elif mean>=70:
                grade ='C'
            elif mean>=60:
                grade ='D'
            else:
                grade ='F'
            print("-------------------------------------------------")
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(info[0],info[1],info[2],info[3],info[4],mean,grade))    
            print("=================================================")
    elif menu==3:
        find_student = int(input("검색할 학번 입력 : "))
        for info  in student:
            if find_student in info:
                print("=====================성적 조회======================")
                print('이름\t학번\tPython\tR\t통계\t평균\t학점')
                mean = (info[2]+info[3]+info[4]) /3
            grade = ""
            if mean >=90:
                grade ='A'
            elif mean>=80:
                grade ='B'
            elif mean>=70:
                grade ='C'
            elif mean>=60:
                grade ='D'
            else:
                grade ='F'
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(info[0],info[1],info[2],info[3],info[4],mean,grade))    
            print("======================================================")
            
# %%
