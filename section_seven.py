monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

for letter in 'hello':
    print(letter)

#Accessing dictionaries in loops
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.values():
    print(grades)

phonebook = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phonebook.items():
    print(f"{key}: {value}")

#While loops
username = ""

while username != "pypy":
    username = input("Enter username: ")