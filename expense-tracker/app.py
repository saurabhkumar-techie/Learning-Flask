
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "expenses.db"


# Connect to database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create database and table
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def index():
    conn = get_db_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY id DESC"
    ).fetchall()

    result = conn.execute(
        "SELECT SUM(amount) FROM expenses"
    ).fetchone()

    total_expenses = result[0] if result[0] is not None else 0

    conn.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total_expenses=total_expenses
    )


# Add expense page
@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount_text = request.form.get("amount", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()

        if not title or not amount_text or not category:
            return "Please fill all required fields.", 400

        try:
            amount = float(amount_text)

            if amount <= 0:
                return "Amount must be greater than zero.", 400

        except ValueError:
            return "Please enter a valid amount.", 400

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO expenses (title, amount, category, description)
            VALUES (?, ?, ?, ?)
            """,
            (title, amount, category, description)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add_expense.html")


# Delete expense
@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# Start application
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
