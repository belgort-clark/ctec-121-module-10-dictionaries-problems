# CTEC 121
# Python Dictionaries Demo
# Part 2
# by Bruce Elgort

def main():
    # dictionary of students
    students = {'Bruce': {'age': 57, 'program': 'Web Development', "gpa": 3.9},
                'Gayle': {'age': 59, 'program': 'Digital Media Arts', "gpa": 3.8},
                'Tommy': {'age': 15, 'program': 'Automotive', "gpa": 2.8},
                'Tracy': {'age': 25, 'program': 'Professional Baking', "gpa": 4.0},
                'Ashlyn': {'age': 18, 'program': 'Culinary', "gpa": 3.9}
                }

    # show Bruce's age
    print(students['Bruce']['age'])
    print()
    # show Tracy's program
    print(students['Tracy']['program'])
    print()

    # Loop thru all student data

    for i, j in students.items():
        print("Student Name:", i)
        for k, m in j.items():
            print("Item:", k, "Value:", m)
        print()


main()
