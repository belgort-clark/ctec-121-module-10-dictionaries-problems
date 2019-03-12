# CTEC 121
# Python Dictionaries Demo
# Part 2
# by Bruce Elgort
# example01.py

def main():
    # dictionary of students
    students = {'Bruce':{'age':53,'gender':'male',"gpa":3.9},
                'Gayle':{'age':55,'gender':'female',"gpa":3.8},
                'Joe':{'age':15,'gender':'male',"gpa":2.8},
                'Tracy':{'age':25,'gender':'female',"gpa":4.0},
                'Ashlyn':{'age':18,'gender':'female',"gpa":3.9}
    }

    # show Bruce's age
    print(students['Bruce']['age'])
    print()
    # show Tracy's gender
    print(students['Tracy']['gender'])
    print()

    # Loop thru all student data

    for i,j in students.items():
        print("Student Name:",i)
        for k,m in j.items():
            print("Item:",k,"Value:",m)
        print()

main()
   
