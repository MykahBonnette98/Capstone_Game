from flask import Flask, render_template, url_for, redirect, request, flash,session
from flask_login import login_user, logout_user
from models import UserModel, db, login
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/highscore": {"origins": "http://127.0.0.1:5000"}})
app.config.from_pyfile("config.py")

db.init_app(app)
login.init_app(app)
login.login_view = "login"
basedir = os.path.abspath(os.path.dirname(__file__))

@app.before_first_request
def create_all():
    db.create_all()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        user = UserModel.query.filter_by(email=email).first()
        session['username'] = user.username
        session['highscore'] = user.highscore
        if user is not None and user.check_password(request.form["password"]):
            login_user(user)
            return render_template("game.html")  
    else:
        return render_template('login.html')
         
@app.route("/register", methods=["POST", "GET", "PUT"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        if UserModel.query.filter_by(email=email).first():
            flash("Email already Present")
            return render_template("login.html")
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("register"))
    return render_template("game.html")

@app.route("/logout")
def logout():
    logout_user()
    session.pop('username', None)
    return render_template('login.html')

@app.route("/highscore", methods=['GET', 'POST'])
def highscore():
    data = request.values
    user = UserModel.query.filter_by(highscore)
    session['highscore'] = user.highscore
    return render_template("profile.html", data=data)

@app.route("/game", methods=['GET','POST','PUT'])
def game():
    return render_template("game.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run()
