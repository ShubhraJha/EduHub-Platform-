from db_models.user_model import get_user_email,create_user
def login_user(email,password):
    user=get_user_email(email) 
    if not user:
        return None, "User not found!"
    if user["password"]!=password:
        return None,"Invalid Password" 
    else:
        return user,None 
def singup_user(email,password):
    if get_user_email(email):
        return None,"User already exist!"
    create_user(email,password,"student")
    user=get_user_email(email)
    return user,None   