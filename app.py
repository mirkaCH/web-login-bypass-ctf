from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = "flag{weak_login_logic}"

HTML = """
<!doctype html>
<html>
<head>
    <title>Admin Login</title>
</head>
<body>
    <h1>Admin Login Portal</h1>
    <p>Only administrators can access this page.</p>

    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Password:</label><br>
        <input type="password" name="password"><br><br>

        <button type="submit">Login</button>
    </form>

    <p>{{ message }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password != "":
            message = f"Welcome admin! Flag: {FLAG}"
        else:
            message = "Access denied."

    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)