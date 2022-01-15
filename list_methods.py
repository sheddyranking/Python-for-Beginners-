numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

numbers.append(7) # add 6
print(numbers)

numbers.insert(0, -1)  #insert -1, before index 0
print(numbers)

numbers.remove(3) #removes 3
print(numbers)

print(1 in numbers) #return bool of TRUE/FALSE if condition meet.

print(len(numbers))

numbers.clear()
print(numbers)