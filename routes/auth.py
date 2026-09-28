from flask import render_template,session,redirect,request,Blueprint 
from services.auth_services import login_user,singup_user 
auth_bp=Blueprint("auth",__name__)
@auth_bp.route("/login",methods=["GET"])
def login_pg():
    return render_template("login.html") 
@auth_bp.route("/login",methods=["POST"]) 
def login():                                           
    email=request.form.get('email')
    password=request.form.get('password')
    if not (email and password):
        msg="*required" 
        return render_template("login.html",msg=msg) 
    user,error=login_user(email,password)
    if not user:
        return render_template("login.html",error=error)
    session["user_id"]= user["user_id"] 
    session["role"]=user["role"]
    if user["role"]=="admin":
        return redirect("/admin")
    elif user["role"]=="teacher":
        return redirect("/")
    else:
        if "next_course" in session:
            course_id = session.pop("next_course")
            batch_id = session.pop("next_batch")

            return redirect(f"/enroll/{course_id}/{batch_id}")

    return redirect("/")
    
@auth_bp.route("/signup",methods=["GET"])
def signup_page():
    return render_template("signup.html") 
@auth_bp.route("/signup",methods=["POST"])
def singup():
    email=request.form.get('email')
    password=request.form.get('password')
    if not (email and password):
        msg="*required" 
        return render_template("signup.html",msg=msg) 
    user,error=singup_user(email,password) 
    if error:
        return render_template("signup.html",error=error) 
    session["user_id"]=user["user_id"]
    session["role"]=user["role"]
    if user["role"]=="student":
        if "next_course" in session:
            course_id = session.pop("next_course")
            batch_id = session.pop("next_batch")
            return redirect(f"/enroll/{course_id}/{batch_id}")

    return redirect("/")

@auth_bp.route("/logout")
def logout():

    session.clear()      # Removes all session data

    return redirect("/")