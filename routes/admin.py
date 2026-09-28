from flask import Blueprint, render_template, session, redirect

from db_models.admin_model import (
    get_admin_stats,
    get_all_students,
    get_all_courses,
    get_all_batches,
    get_all_teachers,
    get_all_enrollments,
    get_all_payments
)


admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    if session.get("role") != "admin":
        return "Access Denied", 403

    stats = get_admin_stats()

    return render_template(
        "admin_dashboard.html",
        stats=stats
    )



@admin_bp.route("/admin/students")
def students():

    if session.get("role") != "admin":
        return "Access Denied", 403

    students = get_all_students()

    return render_template(
        "admin_students.html",
        students=students
    )


# ==========================================
# COURSES
# ==========================================

@admin_bp.route("/admin/courses")
def courses():

    if session.get("role") != "admin":
        return "Access Denied", 403

    courses = get_all_courses()

    return render_template(
        "admin_courses.html",
        courses=courses
    )


# ==========================================
# BATCHES
# ==========================================

@admin_bp.route("/admin/batches")
def batches():

    if session.get("role") != "admin":
        return "Access Denied", 403

    batches = get_all_batches()

    return render_template(
        "admin_batches.html",
        batches=batches
    )


# ==========================================
# TEACHERS
# ==========================================

@admin_bp.route("/admin/teachers")
def teachers():

    if session.get("role") != "admin":
        return "Access Denied", 403

    teachers = get_all_teachers()

    return render_template(
        "admin_teachers.html",
        teachers=teachers
    )


# ==========================================
# ENROLLMENTS
# ==========================================

@admin_bp.route("/admin/enrollments")
def enrollments():

    if session.get("role") != "admin":
        return "Access Denied", 403

    enrollments = get_all_enrollments()

    return render_template(
        "admin_enrollments.html",
        enrollments=enrollments
    )


# ==========================================
# PAYMENTS
# ==========================================

@admin_bp.route("/admin/payments")
def payments():

    if session.get("role") != "admin":
        return "Access Denied", 403

    payments = get_all_payments()

    return render_template(
        "admin_payments.html",
        payments=payments
    )