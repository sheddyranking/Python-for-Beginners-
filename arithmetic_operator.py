#General operator
print(10/3)
print(10+3)
print(10-3)
print(10*3)

print(10//3) #returns an int
print(10**3) #return exponential
print(10%3) #returns remainder

#argurmented 
x= 10
x = x+3 # will return 13
print(x) 

y = 10
y +=3 # will still return 13
print(y)

#therefore it can be -=, *=, or  /= .

#operator precedence

x = 10+3*2 
print(x) #16

y = (10+3)*2
print(y) #26

#Operator comparison

x= 3>2
print(x) #return a bool of TRUE 

#we also have <, <=, >=, ==, !=

#logical operators

price = 10

print(price > 5 and price < 30) #returns TRUE
print(price > 10 or price < 15) #return TRUE
print(not price > 15) #return TRUE

#and (TRUE when both condition meet else FALSE)
#or(TRUE if of the conditions meet else FALSE)
#not(TRUE when TRUE or FALSE when FALSE)

