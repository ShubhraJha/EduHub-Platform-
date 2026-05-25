from flask import Blueprint, render_template
from db_model.course_model import get_full_data
from services.course_service import build_structure

course_bp = Blueprint("course", __name__)

# ======================
# 🏠 HOME + CATEGORY (SAME PAGE)
# ======================

@course_bp.route("/")
@course_bp.route("/category/<int:cat_id>")
def home(cat_id=None):
    rows = get_full_data()
    data = build_structure(rows)

    selected_category = None

    if cat_id:
        selected_category = data.get(cat_id)

    return render_template(
        "index.html",
        data=data,
        selected_category=selected_category,
        selected_category_id=cat_id
    )


# ======================
# 📘 COURSE PAGE (BATCH CARDS)
# ======================

@course_bp.route("/course/<int:course_id>")
def course_detail(course_id):
    rows = get_full_data()
    data = build_structure(rows)

    selected_course = None

    for cat in data.values():
        if course_id in cat["courses"]:
            selected_course = cat["courses"][course_id]
            break

    # optional safety
    if not selected_course:
        return "Course not found"

    return render_template("course_details.html", course=selected_course)