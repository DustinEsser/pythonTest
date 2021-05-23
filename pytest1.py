import os

print("hello, welcome to the python learning center!")

def welcomePrintName(str):
    print("Welcome", end = "")
    for x in str:
        print(x)

name = input("Please type your first and last name: ")
welcomePrintName(name.split())