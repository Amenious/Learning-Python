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