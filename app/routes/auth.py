from flask import Blueprint, render_template, request, redirect, session
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password
        })

        return redirect("/login")

    return render_template("register.html")


@auth.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        user = mongo.db.users.find_one({
            "email": email
        })

        print("EMAIL ENTERED:", email)
        print("USER FOUND:", user)

        if user:
            if check_password_hash(user["password"], password):

                session["user"] = user["username"]
                return redirect("/dashboard")

        return "Invalid email or password"

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")