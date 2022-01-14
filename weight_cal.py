weight = int(input("Enter your weight "))
uint = input("(k)g or (L)bs ")

if uint.upper() =="K":
    converted = weight/0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight*0.45
    print("weight in Kgs: " + str(converted))    