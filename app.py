print("APP IS RUNNING")
from db.connection import get_db_con 
db=get_db_con() 
cur=db.cursor() 
cur.execute("SELECT*FROM users")
print(cur.fetchall())
