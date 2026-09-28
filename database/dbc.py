from config import Config 
import pymysql
def get_db_con():
    connection=pymysql.connect (
        host=Config.MYSQL_HOST, 
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD, 
        database=Config.MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor 
        
    ) 
    return connection 
