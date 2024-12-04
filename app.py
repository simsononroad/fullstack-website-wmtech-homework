from flask import Flask, request, render_template, redirect, url_for, flash, session
#import database
import hashlib
import sqlite3

# Felhasználó hazzáadásához szükséges lépések:
#   1. Nézze meg egy másik file-ban hogy a tesztelni kívánt jelszónak mi a kódja.
#   2. hozzon itt létre egy "password_in_hash_x" változót
#   3. A try-on belül hozzon létre egy parancsoot ami beteszi a helyére a felhasználóneve és jelszót

password_in_hash_1 = "4c00da99010ff9be00046e7854e2bd5cfca292ae9c629421ae89b08a5370e91c"
password_in_hash_2 = "c52c5501c5ddd107202a95915b4466f98773b611a09cf8a283ebbe2760f6236a"
password_in_hash_3 = "f854b2aeb789d616b26acff4df9ff7741d09d5f7a63add238201880e5b10bf2b"
con = sqlite3.connect("login.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE login(id INT PRIMARY KEY ,name, password)")
    ins = cur.execute(f"insert into login (name, password) values ('admin', '{password_in_hash_1}')")
    con.commit()
    ins = cur.execute(f"insert into login (name, password) values ('teszt', '{password_in_hash_2}')")
    con.commit()
    ins = cur.execute(f"insert into login (name, password) values ('ok', '{password_in_hash_3}')")
    con.commit()
except:
    pass









app = Flask(__name__)
app.secret_key = "szupertitkoskulcs"  # Ezt cseréld le egy erősebb kulcsra!



# Előre meghatározott felhasználónév és jelszó


# Főoldal (index)
@app.route("/")
def index():
    return render_template("index.html")

# Bejelentkezés
@app.route("/login", methods=["POST"])
def login():
    con = sqlite3.connect("login.db")
    cur = con.cursor()
    username_in_html = request.form['username']
    password_in_html = request.form['password']
    password_hash = hashlib.sha256(password_in_html.encode("UTF-8")).hexdigest()
    username_in_html_felesleggel = f"('{username_in_html}',)"
    password_hash_felesleggel = f"('{password_in_html}',)"
    print("================================")
    print(username_in_html_felesleggel)
    print(password_hash_felesleggel)
    print("================================")
    # Hitelesítés az előre megadott adatokkal
    
    cur.execute(f"SELECT name, password FROM login WHERE name = \"{username_in_html}\"")
    login_in_db = cur.fetchall()
    print(login_in_db)
    
    if len(login_in_db) == 0:
        flash("Helytelen felhasználónév vagy jelszó. \nFelhasználónév: admin || Jelszó:titkos", "error")
        return redirect(url_for("index"))
    if login_in_db[0][1] != password_hash:
        flash("Helytelen felhasználónév vagy jelszó. \nFelhasználónév: admin || Jelszó:titkos", "error")
        return redirect(url_for("index"))
    session["user"] = username_in_html
    flash("Sikeres bejelentkezés!", "success")
    return redirect(url_for("dashboard"))
    
    
    

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
