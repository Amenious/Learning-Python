#creating a mean function
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))

#area of a square
def area(value):
    calc = value * value
    return calc

print(area(7))

#convert ounces to mililiters
def convert(ounces):
    mil = ounces * 29.57353
    return mil

print(convert(5))