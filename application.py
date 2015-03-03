"""Factorial program"""

import os #imports functions to clear
import sys #imports some functions like the one to end program

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def fact(num):
    """Generates the factorial answer"""
    if num == 0:
        return 1
    if num == 1:
        return 1
    if num != 1:
        total = num * fact(num - 1) #recursivity to use the same function
        return total

def enter():
    """Allows the user to enter number """
    print """
    _____________________________________________________________________

    -----------------Welcome to the factorial calculator-----------------
    _____________________________________________________________________
    """
    validate = True #validates the next parts
    while validate == True:
        try: #for later errors
            user = input("Enter a number: ") #asks for a number
            print "The factorial is: ", fact(user) #calls the function with the user variable
            new() #asks the user for another number
            break #ends
        except (ValueError, NameError):
            print "Only enter numbers" #if the user enters letters

def new():
    """Allows the user to enter another number"""
    variable = True #variable to kill later
    while variable == True:
        ask = raw_input("Do you want to enter another number? Y/N: ") #asks for an option
        ask = ask.lower() #converts it into lowercase
        if ask == "y":
            clear()
            enter() #calls the function
        elif ask == "n":
            print "Thank you for playing, bye."
            variable = False
            sys.exit() #command to exit the program
        else:
            print "Only enter Y or N"

enter() #initiates the program
