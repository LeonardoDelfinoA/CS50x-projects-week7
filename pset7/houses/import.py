import csv
from cs50 import SQL
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Error 1. O programa aceita apenas 2 argumentos.")
        quit()
    
    file = open(sys.argv[1])
    reader = csv.DictReader(file)
    db = SQL("sqlite:///students.db")
    
    for row in reader:
        
        split_name = row["name"].split()
        if len(split_name) == 3:
            
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", split_name[0], split_name[1], split_name[2], row["house"], row["birth"])
        
        elif len(split_name) < 3:
            
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", split_name[0], "NULL", split_name[1], row["house"], row["birth"])
        
            


if __name__ == '__main__':
    main()