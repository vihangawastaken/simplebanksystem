import json
from datetime import datetime

from easyFunc import *
from account import *

def mainConsoleWindow() : 
    print("***************************************************************************************")
    print("* This is a simple banking system program developed by VihangaWasTaken (2025)")
    print("* This project is only to improve my own programming skiils")
    print("* Feel free to use the code however you want without limitations")
    print("***************************************************************************************")
    print(" ")
    print('type "help" to list of available commands')
    commandLine()

def commandLine() : 
        commandRan = input("> ")
        if commandRan == "help" :
            helpWindow()
        if commandRan == "exit" :
            exit()
        if commandRan == "checkaccount" :
            loadAccountDetails()
            commandLine()
        if commandRan == "deposit" :
            depositToAccount()
            commandLine()
        if commandRan == "withdraw" :
            withdrawFromAccount()
            commandLine()
        else : 
            print("Unknown command")
            commandLine()

def helpWindow() :
    print("These are the available commands: ")
    print("(1) checkaccount - Check your account information")
    print("(2) withdraw - Withdraw money from your account")
    print("(3) deposit - Deposit money to your account")
    print("(4) exit - Exit")

    commandLine()

mainConsoleWindow()