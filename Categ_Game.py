print("""CATEGORIES K 
WELCOME TO SCRAMBLED 
QUESTION THAT ARE RELATED ON K
RULES IF YOU WRONG ONE QUESTION YOU CAN'T ABLE TO 
PROCEED TO ANOTHER NUMBER!""" )
print(" \nENTER PLAYER NAME")
name=input(" > ")

print(f" HELLO {name} WELCOME TO SCRAMBLED WORDS \n ")
score=0
print("""IF YOU WANT TO START THE SCRAMBLE GAME PLEASE TYPE YES IF YOU DO NOT WANT TO PLAY TYPE NO""")
game=input("> ")
if game=="yes" or game=='Yes' or    game=="YES":
 print("START THE GAME")
 print("1. IKLELR ")
 ans=input("> ")
 if ans=='KILLER' or ans== 'killer':
    print("Your answer is correct")
    score+=1
 else:
       print("Wrong answer")
 print("2. GONKMID")
 ans=input("> ")
 if ans=='KINGDOM' or ans=='kingdom':
               print("Your answer is correct")
               score+=1
 else:
               print("Wrong answer")
 print("3. Gkliorma ")
 ans=input("> ")
 if ans=="Kilogram" or ans=="KILOGRAM":
  print(" Your answer is correct")
  score+=1
 else:
    print("Wrong answer")
 print("4. keora")
 ans=input("> ")
 if ans=="KOREA" or ans=="Korea":
   print(" Your answer is correct")
   score+=1
 else:
      print("Wrong Answer")
 print("5. degwnkoel")
 ans=input("> ")
 if ans=="Knowledge" or ans=="KNOWLEDGE":
  print(" Your answer is correct")
  score+=1
 else:
     print("Wrong Answer")
 print(f"Your total score is {score}")
else:
    print("YOU DONT WANT TO PLAY THIS GAME, THANKYOU!")