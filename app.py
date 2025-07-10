from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("login.html")
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin123":
        return f"Welcome, {username}!"
    return "Invalid credentials"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
