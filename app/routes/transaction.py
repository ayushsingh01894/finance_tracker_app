from flask import Blueprint, render_template, request, redirect, session
from app import mongo
from bson.objectid import ObjectId

transaction = Blueprint("transaction", __name__)

@transaction.route("/add_transaction", methods=["GET","POST"])
def add_transaction():

    # 🔒 Protect route
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        type = request.form["type"]
        category = request.form["category"]
        amount = float(request.form["amount"])
        date = request.form["date"]

        mongo.db.transactions.insert_one({
            "type": type,
            "category": category,
            "amount": amount,
            "date": date
        })

        return redirect("/dashboard")

    return render_template("add_transaction.html")

@transaction.route("/delete/<id>")
def delete_transaction(id):

    if "user" not in session:
        return redirect("/login")

    mongo.db.transactions.delete_one({
        "_id": ObjectId(id)
    })

    return redirect("/dashboard")