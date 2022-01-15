#tuples are list than can't be updated.
# it has two methods, count(), and index()
#the rest with and under_score are called magic methods.
#tuples are declared within ()

numbers = (1, 2, 3, 4, 4)
print(numbers)

print(" ")

count = numbers.count(4) #return the occurance of 4 in the tuple = [2]
print(count)

print(" ")

names = ("sam", "joe", "pat", "krul", "umar", )
print(names)

index = names.index("pat") #return the index of pat  =[2]
print(index)