from flask import request,Blueprint,redirect,render_template,session
from services.auth_services import login_user,register_user 

login_routes=Blueprint("auth", __name__)
@login_routes.route("/login",methods=["GET"])
def login_page():
    return render_template("login.html")

@login_routes.route("/login",methods=["POST"])
def login():
    email=request.form.get("email") 
    password=request.form.get("password")
    user,msg=login_user(email,password)
    if not user:
        return msg 
    session["user_id"]=user["user_id"]
    session["role"] = user["role"] 
    if user["role"]=="admin":
        return redirect("/admin")
    elif user["role"] == "teacher":
        return redirect("/teacher")
    else:
        return redirect("/student") 
    
@login_routes.route("/signup",methods=["GET"])
def signup_page():
    return render_template("signup.html")

@login_routes.route("/signup",methods=["POST"])
def signup():
    email=request.form.get("email")
    password=request.form.get("password")
    user,error = register_user(email, password)
    if error:
        return render_template("signup.html", error=error)
    session["user_id"] = user["user_id"]
    session["role"] = user["role"]

    # redirect like login
    if user["role"] == "admin":
        return redirect("/admin")
    elif user["role"] == "teacher":
        return redirect("/teacher")
    else:
        return redirect("/")

    
        