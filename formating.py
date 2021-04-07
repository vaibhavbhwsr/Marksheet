# imported main and tabulate
import main
from tabulate import tabulate

# Formatting the data inputted through main.py
print("-------------------------------------------------------------------")  # length of this string is 68
print("|" + "S.No. 12345" + "Central Board of Secondary Education".center(46) + "        |")
print("|" + "Senior School Certificate Examination(Class-XII)".center(65) + "|")
print("|                                                                 |")
print(f"| Name: {main.name}" + "|".rjust(59 - len(str(main.name))))
print(f"| Mother Name: {main.mname}" + "|".rjust(52 - len(str(main.mname))))
print(f"| Father Name: {main.fname}" + "|".rjust(52 - len(str(main.fname))))
print(f"| Data Of Birth: {main.DOB}" + "|".rjust(67 - 27))
print(f"| School Name: {main.school}" + "|".rjust(52 - len(str(main.school))))
print("|                                                                 |")
tablelists = [["101 ENGLISH COMM.", f"{main.marks[0]}", "XX", f"{main.marks[0]}", f"{main.grade(main.marks[0])}"],
              ["085 HINDI COURSE-B", f"{main.marks[1]}", "XX", f"{main.marks[1]}", f"{main.grade(main.marks[1])}"],
              ["041 MATHEMATICS", f"{main.marks[2]}", "XX", f"{main.marks[2]}", f"{main.grade(main.marks[2])}"],
              ["086 SCIENCE & TECH", f"{main.marks[3]}", f"{main.marks[5]}", f"{main.marks[3] + main.marks[5]}",
               f"{main.grade(main.marks[3] + main.marks[5])}"],
              ["087 SOCIAL SCIENCE", f"{main.marks[4]}", f"{main.marks[6]}", f"{main.marks[4] + main.marks[6]}",
               f"{main.grade(main.marks[4] + main.marks[6])}"]]
print(tabulate(tablelists, headers=["Subject Name", "Theory", "Practical", "Total", "Grade"], tablefmt="github"))
print("|                                                                 |")
if main.p:
    print("| Result: Pass" + f"Percentage: {main.per}".rjust(52) + "|")
else:
    print("| Result: Fail" + f"Percentage: {main.per}".rjust(52) + "|")

print("-------------------------------------------------------------------")
