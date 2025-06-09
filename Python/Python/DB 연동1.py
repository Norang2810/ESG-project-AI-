# %%
import pymysql

db_connect = pymysql.connect(
    host="localhost",
    port=3306,
    db="ESG_Python",
    user="root",
    passwd="0122",
    charset="utf8",
)  # 한글 깨지는 현상 방지


## cursor() : pymysql 라이브러리 통해서 sql문 호출하고 결과값 담는 기능
db_connected = db_connect.cursor()

sql = """
        insert into user_info values(%s,%s,%s,%s)
    """
    
   
db_connected.execute(sql,("Heyjinu","1234","진우",int(20)))
##모든 작업 정상적으로 처리하겠다고 확정
db_connect.commit()
#db연결 종료
db_connect.close()