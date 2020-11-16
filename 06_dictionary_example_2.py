# CTEC 121
# Python Dictionaries
# 06_dictionary_example_2.py
# Part 1
# by Bruce Elgort

# Learn more about Python Dictionaries https://docs.python.org/3/tutorial/datastructures.html


def main():

    print('Learn more about dictionaries:\nhttps://docs.python.org/3/tutorial/datastructures.html')
    print()

    # dictionary of students
    # key / value pairs of data
    students = {
        'Bruce': 'Python',
        'Ashlyn': 'JavaScript',
        'Aaron': 'Perl',
        'Gayle': 'PHP',
        'William': 'Python',
        'Tristan': 'Python',
        'George': 'Fortran',
        'Sam': 'Java'
    }

    # loop thru items in the dictionary and print out their values
    print("Looping thru dictionary...")
    for student, language in students.items():
        print(student, language)

    print()

    # print specific item in the dictionary
    print("Printing out value of 'Bruce'")
    print(students['Bruce'])

    print()

    # printing out the items in the dictionary sorted
    print("Printing sorted dictionary items...")
    for i, j in sorted(students.items()):
        print(i, j)

    print()

    # change value of a dictionary item
    print("Changing value of 'Bruce' to unknown...")
    students['Bruce'] = 'unknown'
    print(students['Bruce'])


main()
