from flask import Flask,render_template
from routes.auth_routes import login_routes
from db_model.course_model import get_full_data
from services.course_service import build_structure

app = Flask(__name__)

# 👉 required for session (login system)
app.secret_key = "secret_key_change_later"

# 👉 register routes
app.register_blueprint(login_routes) 


@app.route("/admin")
def admin():
    return "Admin Dashboard"


@app.route("/teacher")
def teacher():
    return "Teacher Dashboard"


@app.route("/student")
def student():
    return "Student Dashboard"

@app.route("/")
def home():
    rows = get_full_data()        # raw DB data
    data = build_structure(rows)  # structured data

    return render_template("index.html", data=data)

# ======================
# 👉 RUN SERVER
# ======================

if __name__ == "__main__":
    app.run(debug=True)