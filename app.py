from flask import Flask,render_template
<<<<<<< HEAD
from routes.auth_routes import login_routes
from routes.course_auth import course_bp 

app = Flask(__name__)

=======
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
>>>>>>> backup-new-work
# 👉 required for session (login system)
app.secret_key = "secret_key_change_later"

# 👉 register routes
<<<<<<< HEAD
app.register_blueprint(login_routes)
app.register_blueprint(course_bp) 

=======
>>>>>>> backup-new-work
@app.route("/admin")
def admin():
    return "Admin db"

<<<<<<< HEAD

@app.route("/teacher")
def teacher():
    return "Teacher Dashboard"


@app.route("/student")
def student():
    return "Student Dashboard"

=======
from routes.student import student_bp

app.register_blueprint(student_bp)
from routes.teacher import teacher_bp

app.register_blueprint(teacher_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(video_bp)
>>>>>>> backup-new-work
# ======================
# 👉 RUN SERVER
# ======================

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True) 
>>>>>>> backup-new-work
