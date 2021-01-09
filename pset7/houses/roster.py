import csv
from cs50 import SQL
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Error 1. O programa aceita apenas 2 argumentos.")
        quit()
    
    house = sys.argv[1]    
    db = SQL("sqlite:///students.db")
    student_by_house = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last", house)
    counter = 0    
    while counter < len(student_by_house):
        if student_by_house[counter].get("middle") == "NULL":
            print("{} {}, born {}".format(student_by_house[counter].get("first"), student_by_house[counter].get("last"), student_by_house[counter].get("birth")))
        else:
            print("{} {} {}, born {}".format(student_by_house[counter].get("first"), student_by_house[counter].get("middle"), student_by_house[counter].get("last"), student_by_house[counter].get("birth")))
            
        counter += 1
if __name__ == '__main__':
    main()