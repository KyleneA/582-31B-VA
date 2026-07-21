import os
from dotenv import load_dotenv

from flask import (Flask, flash, redirect, render_template, request, url_for)
from flask_login import (LoginManager, current_user, login_required, login_user, logout_user)

from models import db, Member

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///foundry.db")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

#db
db.init_app(app)

#login
login_manager = LoginManager()
login_manager.login_view = "login"

login_manager.init_app(app)

with app.app_context():
    db.create_all()

# loading the user
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Member, int(user_id))

# registering user
def validate_password(password):
    #password: 8-20 characters
    if len(password) < 8:
        return("password must contain at least 8 characters")
    
    if len(password) > 20:
        return("password must contain at most 20 characters")
    
    # checking for uppercase
    if not any(character.isupper() for character in password):
        return ("Password must contain at least one uppercase letter")
    
    # checking for number
    if not any(character.isdigit() for character in password):
        return ("Password must contain at least one digit")
    
    # if valid password
    return None

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        errors = []

        if not username:
            errors.append("Username is required")

        if len(username) > 50:
            errors.append("Username may contain at most 50 characters")
        
        if any(character.isspace() for character in username):
            errors.append("Username may not contain whitespace")
        
        existing_username = Member.query.filter_by(username=username).first()

        if existing_username:
            errors.append("Username is already in use")
        
        existing_email = Member.query.filter_by(email=email).first()

        if existing_email:
            errors.append("Email is already registered")
        
        password_error = validate_password(password)

        if password_error:
            errors.append(password_error)

        if errors:
            for error in errors:
                flash(error, "error") # second argument becomes the category and can be used to set class names for styling etc.
            
            return render_template("register.html", username=username, email=email)

        member = Member(username=username, email=email)

        member.set_password(password)

        db.session.add(member)
        db.session.commit()

        flash("Your account has been created")
    
        return redirect(url_for("login"))
        
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        member = Member.query.filter_by(username=username).first()
        
        if member is None or not member.check_password(password):
            flash("Invalid username or password", error)

            return render_template("login.html", username=username)
    
        login_user(member)
        flash("Your now logged in.", "success")

        return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()

    flash("You have been logged out", "success")
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    workshops = [
        {
            "title": "Intro to Screen Printing",
            "date": "August 8",
            "spaces": 6,
        },
        {
            "title": "Arduino for Beginners",
            "date": "August 12",
            "spaces": 3,
        },
        {
            "title": "Woodworking Basics",
            "date": "August 18",
            "spaces": 0,
        },
    ]
    return render_template("dashboard.html", workshops=workshops)

@app.route("/account")
@login_required
def account():
    return render_template("account.html")

# changing email
@app.route("/account/email", methods=["POST"])
@login_required
def change_email():
    email = request.form["email"].strip().lower()

    if not email:
        flash("Email is required!", "error")

        return redirect(url_for("account"))
    
    existing_member = Member.query.filter(Member.email == email, Member.id != current_user.id).first()

    if existing_member:
        flash("Email is already registered", "error")
        return redirect(url_for("account"))

    current_user.email = email
    db.session.commit()

    flash("Your email was updated", "success")

    return redirect(url_for("account"))

# changing password
@app.route("/account/password", methods=["POST"])
@login_required
def change_password():
    current_password = request.form["current_password"]
    new_password = request.form["new_password"]

    if not current_user.check_password(current_password):
        flash("Current password is incorrect", "error")
        return redirect(url_for("account"))

    password_error = validate_password(new_password)

    if password_error:
        flash(password_error, "error")
        return redirect(url_for("account"))
    
    current_user.set_password(new_password)

    db.session.commit

    flash("Your password was updated", "success")

    return redirect(url_for("account"))

# Home
@app.route("/")
def home():
    return render_template("home.html")