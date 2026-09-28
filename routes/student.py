from flask import Blueprint, request, redirect, render_template, session

from services.enrollment_service import confirm_enrollment
from services.student_service import is_profile_complete
from db_models.student_model import create_student
from db_models.enrollment_model import get_student_courses
from services.lecture_service import get_batch_lectures
from database.dbc import get_db_con

student_bp = Blueprint("student", __name__)


# ==========================================
# COMPLETE PROFILE PAGE
# ==========================================

@student_bp.route("/student/complete-profile")
def complete_profile():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("complete_profile.html")


# ==========================================
# SAVE PROFILE
# ==========================================

@student_bp.route("/student/complete-profile", methods=["POST"])
def save_profile():

    student_id = session["user_id"]

    create_student(
        student_id,
        request.form["name"],
        request.form["student_phone"],
        request.form["parent_phone"],
        request.form["gender"],
        request.form["dob"],
        request.form["address"]
    )

    batch_id = session.pop("pending_batch_id")
    txn_id = session.pop("pending_txn_id")

    confirm_enrollment(
        student_id,
        batch_id,
        txn_id
    )
    session["has_course"] = True

    return redirect("/student/dashboard")

# ==========================================
# CONFIRM ENROLLMENT
# ==========================================

@student_bp.route("/confirm-enrollment", methods=["POST"])
def enroll():

    if "user_id" not in session:
        return redirect("/login")

    student_id = session["user_id"]

    batch_id = request.form["batch_id"]
    txn_id = request.form["transaction_id"]

    if not is_profile_complete(student_id):

        session["pending_batch_id"] = batch_id
        session["pending_txn_id"] = txn_id

        return redirect("/student/complete-profile")
    confirm_enrollment(
    student_id,
    batch_id,
    txn_id
)
    session["has_course"] = True
    return redirect("/student/dashboard")
# ==========================================
# STUDENT DASHBOARD
# ==========================================

@student_bp.route("/student/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    student_id = session["user_id"]

    courses = get_student_courses(student_id)
    if not courses:
        return redirect("/")

    session["has_course"] = True


    return render_template(
        "student_dashboard.html",
        courses=courses
    )
    
@student_bp.route("/course/<int:batch_id>")
def course(batch_id):

    lectures = get_batch_lectures(batch_id)

    return render_template(
        "course_page.html",
        lectures=lectures,
        batch_id=batch_id
    )


@student_bp.route("/watch/<int:lecture_id>")
def watch(lecture_id):

    db = get_db_con()

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM lectures WHERE lecture_id=%s",
        (lecture_id,)
    )

    lecture = cur.fetchone()

    cur.close()
    db.close()

    return render_template(
        "watch_video.html",
        lecture=lecture
    )