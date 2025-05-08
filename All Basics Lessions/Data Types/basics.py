#These are variables
#Integer
x = 10
#String
y = "Hello"
#Float
z = 10.1

#This is a list. This is mutable
student_grades = [9.1, 8.8, 7.5]
#This is a Dictionary
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
#This is a tuple. This is immutable
monday_temperatures = (1, 4, 5)

#This is a range
fun_range = list(range(1, 9, 2))

#print(fun_range)

#Average of student grades
mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length

print(mean)