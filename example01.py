# CTEC 121
# Python Dictionaries Demo
# by Bruce Elgort
# example01.py

def main():

    print('Learn more about dictionaries:\nhttps://docs.python.org/3/tutorial/datastructures.html')
    print()
    
    # dictionary of students
    students = {
                'Bruce':'male',
                'Ashlyn':'female',
                'Aaron':'male',
                'Gayle':'female',
                'William':'male',
                'Tristan':'male'
    }

    # loop thru items and their values
    print("Looping thru dictionary...")
    for i,j in students.items():
        print(i,j)

    print()
    
    # print specific item in the dictionary
    print("Printing out value of 'Bruce'")
    print(students['Bruce'])

    print()
    
    # print them out sorted
    print("Printing sorted dictionary items...")
    for i,j in sorted(students.items()):
        print(i,j)

    print()

    # change value of a dictionary item
    print("Changing value of 'Bruce' to unknown...")
    students['Bruce'] = 'unknown'   
    print(students['Bruce'])
    
main()
