import pymysql 
def get_db_con():
    connection=pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database="edu_online",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection  