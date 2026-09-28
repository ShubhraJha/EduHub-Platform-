from flask import Flask,render_template
from routes.course import course_bp 
from routes.auth import auth_bp
from routes.subject import subject_bp
from routes.video import video_bp
from routes.admin import admin_bp
app = Flask(__name__)
# 👉 register routes
app.register_blueprint(auth_bp)
app.register_blueprint(course_bp)  

app.register_blueprint(admin_bp)
# 👉 required for session (login system)
app.secret_key = "secret_key_change_later"

# 👉 register routes
@app.route("/admin")
def admin():
    return "Admin db"

from routes.student import student_bp

app.register_blueprint(student_bp)
from routes.teacher import teacher_bp

app.register_blueprint(teacher_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(video_bp)
# ======================
# 👉 RUN SERVER
# ======================

if __name__ == "__main__":
    app.run(debug=True) 