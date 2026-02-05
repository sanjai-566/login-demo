# 🔐 Secure Login System (Python GUI)

## 📌 Overview

This project is a **Secure Login and Registration System** built using **Python Tkinter** and **SQLite**. It provides a simple graphical user interface (GUI) that allows users to **register**, **log in**, and access a protected **dashboard**.

Passwords are securely stored using **SHA-256 hashing**, ensuring that plain-text credentials are never saved in the database.

This project demonstrates core concepts of **authentication**, **password security**, and **local database integration**.

---

## 👤 Author

* This project is developed **for educational purposes only**. It is intended for learning authentication concepts and should not be used directly in production systems without additional security enhancements.

---

## 🎯 Objectives

* Implement a secure user authentication system
* Prevent storage of plain-text passwords
* Demonstrate GUI-based login and registration
* Integrate Python applications with SQLite databases
* Apply basic cybersecurity best practices

---

## ⚙️ Features

* User registration with validation
* Secure password hashing (SHA-256)
* Login authentication using hashed credentials
* SQLite database for local storage
* Graphical dashboard after successful login
* Error handling for invalid credentials
* Logout functionality

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **GUI Framework:** Tkinter
* **Database:** SQLite3
* **Security:** SHA-256 Password Hashing
* **Libraries Used:**

  * `tkinter`
  * `sqlite3`
  * `hashlib`

---

## 📂 Project Structure

```
├── login_gui.py     # Main application file
├── users.db         # SQLite database (auto-created)
└── README.md        # Project documentation
```

---

## 🚀 How to Run the Project

1. **Ensure Python 3 is installed**

```bash
python --version
```

2. **Run the application**

```bash
python login_gui.py
```

3. **Create a new account**

* Click on **Create New Account**
* Enter a username and password (minimum 6 characters)

4. **Login to the system**

* Enter registered credentials
* Access the secure dashboard

---

## 🔑 Password Security

* Passwords are hashed using **SHA-256** before storing in the database
* Even if the database is accessed, original passwords cannot be retrieved
* This follows basic authentication security best practices

---

## 📊 Database Details

* Database name: `users.db`
* Table: `users`

### Table Structure

```
username  TEXT (Primary Key)
password  TEXT (Hashed)
```

---

## ⚠️ Disclaimer

This project is developed **for educational purposes only**. It is intended for learning authentication concepts and should not be used directly in production systems without additional security enhancements.

---

## 📘 Use Cases

* Academic mini-projects
* Python GUI learning
* Authentication system demonstration
* Cybersecurity fundamentals practice

---

---

📝 *Note: This README is a template. Please customize personal details before submission or public sharing.*
