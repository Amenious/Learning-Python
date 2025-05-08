#creating a mean function
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

#print(mean([1, 4, 5]))

#area of a square
def area(value):
    calc = value * value
    return calc

#print(area(7))

#convert ounces to mililiters
def convert(ounces):
    mil = ounces * 29.57353
    return mil

#print(convert(5))


#Conditional
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades))

#Quiz
def foo(x, array):
    if x in array:
        return True
    else:
        return False
     
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))