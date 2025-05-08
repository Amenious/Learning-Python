monday_temperatures = [9.1, 8.8, 7.5]

#Adds to list
monday_temperatures.append(2.4)

#These do the same thing
monday_temperatures.__getitem__(1)
monday_temperatures[1]

#Interesting Exercise. Addes to an existing list with getitem call
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'] 
weekends = ['saturday', 'sunday']

weekdays.append(weekends[0])
print(weekdays)

tuesday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]

data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
print(data['b'][2])