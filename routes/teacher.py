from flask import Blueprint, render_template, session

teacher_bp = Blueprint("teacher", __name__)

@teacher_bp.route("/teacher/dashboard")
def teacher_dashboard():

    teacher_id = session["user_id"]

    return render_template("teacher_dashboard.html")