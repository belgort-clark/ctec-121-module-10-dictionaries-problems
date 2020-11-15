# CTEC 121
# Dictionaries
# 05_dictionary_example_1.py
# Use Dictionaries to store Key / Value pairs

# create an empty dictionary
students = {}

# A dictionary of student names and their student ID's
students = {'Bruce Elgort': 940000000, 'Joe Blow': 940111111, 'Gayle Ujifusa': 940222222}

# Print out the value for key 'Bruce Elgort'
print(students['Bruce Elgort'])
print()

# Iterate through a dictionary using a loop
# Note .items()
# Note i,j
# i = key
# j = value
for i, j in students.items():
    print(i, j)

# delete a key/value pair
del students['Bruce Elgort']

# note that Bruce Elgort has been removed
print(students)
print()

# in
print('Gayle Ujifusa' in students)
print('Eric Powers' in students)
print()

# new dictionary of students
students = {'Bruce': ['Male', 4.0, 'AAT'], 'Eric': ['Alien', 3.9, 'AA']}

# Iterate through the dictionary keys
for i, j in students.items():
    # print the key
    print(i)
    # iterate through the list values
    for values in j:
        print("-", values)
