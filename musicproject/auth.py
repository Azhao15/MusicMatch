import re

from flask import (
    Blueprint, flash, redirect, render_template, request, session
)
from werkzeug.security import check_password_hash, generate_password_hash
from musicproject.database import db_session
from .database import User
from functools import wraps

bp = Blueprint('login', __name__, url_prefix='/')


# declare if endpoints require a login
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via GET
    if request.method == "GET":
        return render_template("login.html")
   
    # User reached route via POST
    else:
        # get user input
        username = request.form.get("username")
        password = request.form.get("password")
        
        # check that all fields were entered
        if not username:
            flash("Username required")
            return redirect("/login")
        elif not password:
            flash("Password required.")
            return redirect("/login")

        # check if password matches username
        rows = db_session.execute("SELECT * FROM users WHERE username = :u",{'u':username}).first()
        if not rows or not check_password_hash(rows["password"], password):
            flash("Incorrect password or username.")
            return redirect("/login")

        # set the session id to the current user's id
        session["user_id"] = rows["id"]

        # redirect to home page
        return redirect("/home")
   
@bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

@bp.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")
    
    else:
        # take in user inputs
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation =request.form.get("confirmation")

        # check that all fields were entered
        if not firstname:
            flash("Must provide first name.")
            return redirect("/register")
        elif not lastname:
            flash("Must provide last name.")
            return redirect("/register")
        elif not email:
            flash("Must provide email.")
            return redirect("/register")
        elif not password:
            flash("Must provide password.")
            return redirect("/register")
        elif not confirmation:
            flash("Must re-type password.")
            return redirect("/register")

        
        # check if username is already taken
        user = db_session.execute("SELECT * FROM users WHERE username = :u",{'u':username}).first()
        if user:
            flash("Username taken.")
            return redirect("/register")
        # simple pattern checker for valid email
        elif not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Please enter a valid email.")
            return redirect("/register")
        # check if passwords match
        elif password != confirmation:
            flash("Password do not match.")
            return redirect("/register")

        # add user's info to users database
        u = User(first_name=firstname, last_name=lastname, email=email,username=username, password=generate_password_hash(password))
        db_session.add(u)
        db_session.commit()

        flash("Thank you for creating an account! Please login below!")
        
        # redirect to the login page
        return redirect("/login")
        
