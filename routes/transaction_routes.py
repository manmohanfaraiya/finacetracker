from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from extensions import db

transaction = Blueprint("transaction", __name__)

# Transaction Model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    type = db.Column(db.String(10))
    category = db.Column(db.String(50))
    date = db.Column(db.String(20))


@transaction.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html")


@transaction.route("/add", methods=["POST"])
def add_transaction():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    t = Transaction(
        user_id=session["user_id"],
        amount=request.form["amount"],
        type=request.form["type"],
        category=request.form["category"],
        date=request.form["date"]
    )

    db.session.add(t)
    db.session.commit()

    return redirect(url_for("transaction.dashboard"))


@transaction.route("/get-data")
def get_data():
    if "user_id" not in session:
        return jsonify([])

    data = Transaction.query.filter_by(user_id=session["user_id"]).all()

    result = []
    for t in data:
        result.append({
            "id": t.id,
            "amount": t.amount,
            "type": t.type,
            "category": t.category,
            "date": t.date
        })

    return jsonify(result)

@transaction.route("/delete/<int:id>", methods=["POST"])
def delete_transaction(id):
    if "user_id" not in session:
        return jsonify({"success": False, "error": "Unauthorized"}), 401

    t = Transaction.query.get(id)
    if t and t.user_id == session["user_id"]:
        db.session.delete(t)
        db.session.commit()
        return jsonify({"success": True})
    
    return jsonify({"success": False, "error": "Transaction not found"}), 404