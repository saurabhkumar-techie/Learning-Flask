# Expense Tracker

This is a simple Expense Tracker project made using Python and Flask. I made this project to practice Flask, HTML, CSS, and working with a database.

## Features

- Add new expenses
- View all expenses
- Calculate total expenses automatically
- Delete expenses
- Add expense categories
- Add an optional description
- Store expenses in an SQLite database
- Simple and responsive website design

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure

```text
expense-tracker/
│
├── app.py
├── expenses.db
│
├── templates/
│   ├── index.html
│   └── add_expense.html
│
└── static/
    └── style.css
```

## How to Run

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd expense-tracker
```

**3. Install Flask**

```bash
pip install flask
```

**4. Run the application**

```bash
python app.py
```

**5. Open the website**

Go to this address in your browser:

```text
http://127.0.0.1:5000/
```

## Database

This project uses SQLite to store expenses. The database and expenses table are created automatically when the application starts.

## What I Learned

- Creating a web application using Flask
- Working with Flask routes
- Handling HTML forms
- Connecting Python with SQLite
- Inserting, reading, and deleting database records
- Using HTML and CSS to create a simple website

## Future Improvements

- Add expense editing functionality
- Filter expenses by category
- Add monthly expense reports
- Display expense charts
- Add user login and registration

## Author

Made by me as a practice project while learning Python and Flask.
