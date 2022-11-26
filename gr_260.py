name = input("Enter your name : ")
section = input("Enter your section : ")

print("\nPlease put your grades in every subject.")

sub1 = float(input("\nEthics : "))
sub2 = float(input("Understanding the Self : "))
sub3 = float(input("Mathematics in the Modern World : "))
sub4 = float(input("Computer Programming 1 : "))

sum = sub1 + sub2 + sub3 + sub4
average = (sub1 + sub2 + sub3 + sub4) /4

print("\n",name)
print(section)
print(average)

a = 5
b = 10
if a <= 10:
    if average >= 96 and 96 <=100:
        print("\nYOUR TOP 1 AND HAVE BEEN PROMOTED TO SECOND SEMESTER!")
    elif average >= 91 and 91 <= 95:
        print("\nYOUR TOP 2 AND HAVE BEEN PROMOTED TO SECOND SEMESTER!")
    elif average >= 85 and 85 <= 90:
        print("\nYOUR TOP 3 AND HAVE BEEN PROMOTED TO SECOND SEMESTER!")
    elif average >= 50 and 50 <= 85:
        print("\nYOU PASSED THIS SEMESTER.")    
    elif average >= 50 and 50 <= 49:
        print("\nSORRY YOU FAILED THIS SEMESTER.")
    else:
        print("\nYOU FAILED!")
else:
    print("\nINVALID GRADES! TRY AGAIN!")
               