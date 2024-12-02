from flask import Flask, request, render_template, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "szupertitkoskulcs"  # Ezt cseréld le egy erősebb kulcsra!

# Előre meghatározott felhasználónév és jelszó
VALID_USERNAME = "admin"
VALID_PASSWORD = "titkos"

# Főoldal (index)
@app.route("/")
def index():
    return render_template("index.html")

# Bejelentkezés
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Hitelesítés az előre megadott adatokkal
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        session["user"] = username
        flash("Sikeres bejelentkezés!", "success")
        return redirect(url_for("dashboard"))
    else:
        flash("Helytelen felhasználónév vagy jelszó. \nFelhasználónév: admin || Jelszó:titkos", "error")
        return redirect(url_for("index"))

# Dashboard (csak bejelentkezett felhasználóknak)
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("Először jelentkezz be!", "error")
        return redirect(url_for("index"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/motor")
def motor():
    if "user" not in session:
        flash("Először jelentkezz be!", "error")
        return redirect(url_for("index"))
    return render_template("moto.html", user=session["user"])
@app.route("/profil")
def profil():
    if "user" not in session:
        flash("Először jelentkezz be!", "error")
        return redirect(url_for("index"))
    return render_template("profil.html", user=session["user"])
@app.route("/4t")
def negy_utem():
    if "user" not in session:
        flash("Először jelentkezz be!", "error")
        return redirect(url_for("index"))
    return render_template("4t.html", user=session["user"])

# Kijelentkezés
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Sikeres kijelentkezés.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
