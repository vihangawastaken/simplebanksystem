# 🏦 Simple Banking System (Python)

This is a simple command-line banking system built with Python. It allows users to manage bank accounts using a JSON file as storage. Users can deposit, withdraw, and authenticate using account number, expire date, and security code.

## 📁 Project Structure

banking-system/
├── main.py
├── account.py
├── accounts.json
└── README.md

## 🔧 Features

- Load accounts from a JSON file
- Deposit money into an account
- Withdraw money from an account (with expire date & security code validation)
- Check if an account is expired
- Save updated balances back to the JSON file

## 📦 Requirements

- Python 3.x

## ▶️ How to Run

1. Clone the repository or download the project folder.

2. Ensure `accounts.json` has valid content. Example:

json
[
  {
    "accountNumber": "1001",
    "owner": "Vihanga",
    "balance": 5000,
    "expireDate": "2030-12-31",
    "securityCode": "7890"
  }
]
Run the main program:

"python main.py"


🔐 Security Notes
Security codes and expire dates are required for withdrawals.

Expired accounts are automatically blocked from transactions.

🧠 Future Improvements
Add support for user registration

Store data in a real database

Add GUI interface

Password hashing for better security

📄 License
This project is open-source and free to use under the MIT License.
