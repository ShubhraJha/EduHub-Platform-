from flask import Flask,render_template
from routes.auth_routes import login_routes
from routes.course_auth import course_bp 

app = Flask(__name__)

# 👉 required for session (login system)
app.secret_key = "secret_key_change_later"

# 👉 register routes
app.register_blueprint(login_routes)
app.register_blueprint(course_bp) 

@app.route("/admin")
def admin():
    return "Admin db"


@app.route("/teacher")
def teacher():
    return "Teacher Dashboard"


@app.route("/student")
def student():
    return "Student Dashboard"

# ======================
# 👉 RUN SERVER
# ======================

if __name__ == "__main__":
    app.run(debug=True)