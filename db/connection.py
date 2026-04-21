import pymysql

def get_db_con():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database="edu_online",
        cursorclass=pymysql.cursors.DictCursor
    )