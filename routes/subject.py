from flask import Blueprint, render_template

from db_models.subject_model import get_subjects

subject_bp = Blueprint("subject", __name__)


@subject_bp.route("/subjects/<int:course_id>")
def subjects(course_id):

    subjects = get_subjects(course_id)

    return render_template(
        "subjects.html",
        subjects=subjects
    )