from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Membuat database & tabel user jika belum ada
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()

# Tambah user default
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
conn.commit()

# Template login (HTML sederhana)
login_page = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
<h2>🔐 Login</h2>
<form method="post">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
<p>{{ msg }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ❗️ Query raw (rentan SQL Injection)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        result = c.execute(query).fetchone()

        if result:
            msg = f"✅ Login berhasil! Selamat datang, {username}"
        else:
            msg = "❌ Login gagal!"

    return render_template_string(login_page, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
