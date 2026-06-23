from flask import Blueprint, render_template, session, redirect
from app import mongo

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
@dashboard.route("/dashboard")
def dashboard_page():

    # 🔒 Protect route
    if "user" not in session:
        return redirect("/login")

    transactions = list(mongo.db.transactions.find())

    income = 0
    expense = 0

    for t in transactions:
        if t["type"] == "income":
            income += t["amount"]
        else:
            expense += t["amount"]

    balance = income - expense

    return render_template(
        "dashboard.html",
        income=income,
        expense=expense,
        balance=balance,
        transactions=transactions
    )