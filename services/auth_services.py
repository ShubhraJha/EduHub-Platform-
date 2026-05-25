from db_model.user_model import get_user_email,create_user 
def login_user(email,password):
    user=get_user_email(email)
    
    if not user:
        return None,"User not found"
    if user["password"]!=password: 
        return None,"Invalid password"
    else:
        return user,None
def register_user(email, password):

    if get_user_email(email):
        return None,"User already exists"

    create_user(email, password, "student")

    user = get_user_email(email)  # fetch fresh record

    return user, None
    