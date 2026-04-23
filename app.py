from flask import Flask,render_template
from routes.auth_routes import login_routes

app = Flask(__name__)

# 👉 required for session (login system)
app.secret_key = "secret_key_change_later"

# 👉 register routes
app.register_blueprint(login_routes) 


# ======================
# 👉 BASIC ROUTES (optional)
# ======================


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
    return render_template("index.html")

# ======================
# 👉 RUN SERVER
# ======================

if __name__ == "__main__":
    app.run(debug=True)