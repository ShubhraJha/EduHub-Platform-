from flask import Blueprint, render_template

from db_models.video_model import get_videos

video_bp = Blueprint("video", __name__)


@video_bp.route("/videos/<int:subject_id>")
def videos(subject_id):

    videos = get_videos(subject_id)

    return render_template(
        "videos.html",
        videos=videos
    )
