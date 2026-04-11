<<<<<<< HEAD
# finacetracker
Finance Income &amp; Expense Tracker is a web app to manage daily finances. Users can add, update, and categorize transactions easily. Built with HTML, CSS, JavaScript, Python (Flask), and MySQL, it provides a simple dashboard for tracking financial data. Git is used for version control.
=======
# Personal Finance App

A sleek, premium Personal Finance Dashboard built with Flask, SQLite, and Vanilla HTML/CSS (styled with Glassmorphism). This app allows users to register, login, and track their expenses and income with dynamic visualizations.

## Features
- **User Authentication**: Secure Sign-up, Login, and Logout functionality using password hashing.
- **Glassmorphism UI**: A beautiful gradient background and semi-transparent frosted glass design natively built with CSS.
- **Dashboard Analysis**: 
  - Dynamic Income vs Expense Doughnut Chart.
  - Expense Trend Line Chart over time.
  - Summary cards tracking Total Balance, Income, and Expense.
- **Transaction Ledger**: Instantly add items to the ledger securely stored in the SQLite database, and instantly delete using the dashboard Interface.

## Prerequisites
Make sure you have **[Python](https://www.python.org/downloads/)** installed on your system.

## Setup & Running Locally (Step-by-Step)

### 1. Clone or Download the project
Download the project folder and open it in a code editor like **VS Code**. 
Open a terminal in the project directory.

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment so the app dependencies don't mix with your global system dependencies.
Run the following command in the terminal:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment\
Before installing anything, activate the environment.
- **On Windows (Command Prompt / PowerShell)**:
  ```bash
  venv\Scripts\activate
  ```
- **On Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```
*(You will see `(venv)` appear at the beginning of your terminal line).*

### 4. Install Dependencies
Install all the required Python libraries (Flask, SQLAlchemy, Chart tools, etc.) using the `requirements.txt` file setup for you.
```bash
pip install -r requirements.txt
```

### 5. Run the Application
Finally, start the Flask Server. Simply run:
```bash
python app.py
```

### 6. Open in Browser
You will see a message in the terminal saying `* Running on http://127.0.0.1:5000`. 
Simply hold `Ctrl` (or `Cmd`) and click the link, or type it into your browser:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

That's it! Register a new account and enjoy your finance tracker!

---

### Database Details
The app comes configured to use **SQLite** out of the box so that it runs effortlessly on your local machine with absolutely zero setup. A `finance.db` file will automatically be created in a hidden `instance/` folder inside the project when you first run `python app.py`. 
>>>>>>> 168fff2 (Added project files)
