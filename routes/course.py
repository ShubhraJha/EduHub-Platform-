from flask import Blueprint, render_template,session,redirect
from db_models.course_model import get_full_data
from services.course_services import build_structure

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

    return render_template("course_details.html", course=selected_course,course_id=course_id) 

@course_bp.route("/enroll/<int:course_id>/<int:batch_id>")
def enroll(course_id, batch_id):

    print(f"Enroll route reached! course_id={course_id}, batch_id={batch_id}")

    # --------------------------------
    # CHECK LOGIN FIRST
    # --------------------------------

    if "user_id" not in session:

        session["next_course"] = course_id
        session["next_batch"] = batch_id

        return redirect("/signup")

    # --------------------------------
    # USER IS ALREADY LOGGED IN
    # Continue normally
    # --------------------------------

    rows = get_full_data()
    data = build_structure(rows)

    batch = None

    for cat in data.values():

        if course_id in cat["courses"]:

            course = cat["courses"][course_id]

            for b in course["batches"]:

                print(f"Checking batch: {b['id']} vs {batch_id}")

                if b["id"] == batch_id:

                    batch = b

                    print(f"Batch found: {batch}")

                    break

    if not batch:
        return f"Batch {batch_id} not found in course {course_id}"

    return render_template(
        "buy.html",
        batch=batch
    )
    