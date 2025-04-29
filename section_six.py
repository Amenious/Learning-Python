def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    
#Takes user input, converts to float from str, and runs function
#user_input = float(input("Enter temperature:"))
#print(weather_condition(user_input))

name = input("Enter your name: ")
surname = input("Enter your surname: ")
#python 2 + 3
message = "Hello %s %s" % (name, surname)
#python 3.6+
message = f"Hello {name} {surname}"
print(message)