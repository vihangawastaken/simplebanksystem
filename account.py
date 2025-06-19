import json
import os
from easyFunc import *
from datetime import datetime

"""
class Account:
    def __init__(self, accountNumber, owner, balance, expireDate, securityCode):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance
        self.expireDate = expireDate
        self.securityCode = securityCode

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
"""


def loadAccountByNumber(account_number):
    with open("accounts.json", 'r') as file:
        data = json.load(file)
        for acc in data:
            if acc['accountNumber'] == account_number:
                return acc
    return None


def loadAccountToDeposit(account_number, filepath="accounts.json"):
    if not os.path.exists(filepath):
        print("Error: accounts.json file not found.")
        return None, None

    with open(filepath, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Error: accounts.json file is empty or corrupted.")
            return None, None

        for acc in data:
            if acc["accountNumber"] == account_number:
                return acc, data

    return None, data

def loadAccountDetails() :
    accountNumberInputFront = input("Enter your account number: ")
    account = loadAccountByNumber(accountNumberInputFront)

    if account :
        print(f"Account Owner : {account['owner']}")
        print(f"Account Balance : {account['balance']}")
        return
    else :
        print("Account number invalid")
        return

def depositToAccount() :
    accountNumberInputFront = input("Enter your account number: ")
    account, allAccounts = loadAccountToDeposit(accountNumberInputFront)

    if account :
        depositAmmount = input("Enter the amount you want to deposit to your account: ")
        depositAmmountInt = int(depositAmmount)
        account['balance'] += depositAmmountInt
            
        with open("accounts.json", "w") as file:
            json.dump(allAccounts, file, indent=4)
            return

    else :
        print("Account number invalid")
        return

def withdrawFromAccount():
    accountNumberInputFront = input("Enter your account number: ")
    account  = loadAccountByNumber(accountNumberInputFront)

    if account :
        accountExpireDateAuth = input("Enter your account expire date: ")
        accountSecurityCodeAuth = input("Enter your account security code: ")

        if accountExpireDateAuth == account['expireDate'] :
            printDebug("Expire date correct")
            expireDate = datetime.strptime(account['expireDate'], "%Y-%m-%d")
            if expireDate > datetime.today() :
                printDebug("Card upto date")
                
                if accountSecurityCodeAuth == account['securityCode'] :
                    printDebug("Security code correct")
                    withDrawAmmount = input("Enter the ammount you want to withdraw: ")
                    withDrawAmmountInt = int(withDrawAmmount)

                    if withDrawAmmountInt < account['balance'] : 
                        accountToWithdraw, allAccounts = loadAccountToDeposit(accountNumberInputFront)
                        accountToWithdraw['balance'] -= withDrawAmmountInt
                        with open("accounts.json", "w") as file:
                            json.dump(allAccounts, file, indent=4)
                            return
                    else :
                        print("You dont have enough money to withdraw in your account")
                        return
                else :
                    print("Account security code invalid")
                    return


            else :
                print("Your account is expired")
                return
        else : 
            print("Invalid expire date")
            return
    else :
        print("Account number invalid")
        return