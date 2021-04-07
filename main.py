# Importing some necessary modules
import datetime
from colorama import Fore

# declaring variables
marks = []
p = True
Sum = 0
# Getting inputs

# Getting personal Details
while True:
    s_no = input("Enter serial number:")
    if len(s_no) == 5:
        break
    else:
        print("\033[1;31m" + "Value must be of 5 Characters" + "\033[0m")
        continue

name = input("Enter name: ")
mname = input("Enter mother name: ")
fname = input("Enter father name: ")
school = input("Enter the School Name: ")

# Checking Validity of DOB
isValidDate = True
while True:
    try:
        DOB = input("Enter the DOB 'dd/mm/yy': ")
        datetime.datetime.strptime(DOB, '%d/%m/%Y')
        break
    except ValueError:
        print("\033[1;31m" + "Input date is not valid.." + "\033[0m")
        continue

# function to check marks validity


def checkMark(max, mark):
    if mark <= max:
        marks.append(mark)
        if mark < 33 / 100 * max:
            global p
            p = False
        return True
    else:
        print("\033[1;31m" + f"Marks Must be less than: {max}" + "\033[0m")
        return False

# Getting marks Details and assigning pass and fail


print("Enter theory marks for:")
while not checkMark(100, int(input("English Marks: "))):
    pass
while not checkMark(100, int(input("Hindi Marks: "))):
    pass
while not checkMark(100, int(input("Mathematics Marks: "))):
    pass
while not checkMark(70, int(input("Science Marks: "))):
    pass
while not checkMark(80, int(input("Social Science Marks: "))):
    pass

print("Enter practical marks for:")
while not checkMark(30, int(input("Science: "))):
    pass
while not checkMark(20, int(input("Social Science: "))):
    pass

# defines a function to return Grade according to 100 points


def grade(a):
    if a > 90:
        return "A1"
    elif a > 80:
        return "A2"
    elif a > 70:
        return "B1"
    elif a > 60:
        return "B2"
    elif a > 50:
        return "C1"
    elif a > 40:
        return "C2"
    elif a > 30:
        return "D1"
    elif a > 20:
        return "E1"
    elif a > 0:
        return "E2"

# Calculation to print Percentage


for i in marks:
    Sum += i
per = (Sum * 100) / 500
# Outputting the Data
'''
print(f"\nSerial Number: {s_no}")
print(f"Name: {name}")
print(f"Mother Name: {mname}")
print(f"Father's Name: {fname}")
print(f"Date Of Birth: {DOB}")
print(f"School: {school}")
print(f"101 ENGLISH COMM. {marks1[0]} Grade: {grade(marks1[0])}")
print(f"085 HINDI COURSE-B {marks1[1]} Grade: {grade(marks1[1])}")
print(f"041 MATHMATICS {marks1[2]} Grade: {grade(marks1[2])}")
print(f"086 SCIENCE & TECH. {marks1[3] + marks2[0]} Grade: {grade(marks1[3] + marks2[0])}")
print(f"087 SOCIAL SCIENCE {marks1[4] + marks2[1]} Grade: {grade(marks1[4] + marks2[1])}")
'''
