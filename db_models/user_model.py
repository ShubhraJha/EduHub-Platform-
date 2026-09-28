from database.dbc import get_db_con 
def get_user_email(email):
    db=get_db_con()
    cur=db.cursor() 
    cur.execute("Select* from users WHERE email=%s" ,(email,))
    user=cur.fetchone() 
    cur.close() 
    db.close() 
    return user 
def create_user(email,password,role):
    db=get_db_con() 
    cur=db.cursor()
    cur.execute("INSERT INTO users(email,password,role) VALUES(%s,%s,%s)",(email,password,role))
    db.commit() 
    cur.close()
    db.close()
    
