print("Let's play a game")
print("You choose a number and the program will tell you the color hiding on your number. ")
print("You should choose from 8 to 11. ")

a = int(input("Make your choose here "))

if a == 8:
    print("GREEN")
elif a == 9:
     print("RED") 
elif a == 10:
     print("BLUE")
elif a == 11:
     print("ORANGE")
else:
     print("Error, you didn't choose a number from 1 to 4. ")