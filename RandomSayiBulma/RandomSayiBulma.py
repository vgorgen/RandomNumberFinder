from random import Random, randint


randomnumber = randint(0,100)
hak = 7
while(hak > 0):
    hak-=1
    guessnumber = int(input("number: "))
    
    if(guessnumber > randomnumber):
        print("Down")
    elif(guessnumber < randomnumber):
        print("Up")
    elif(guessnumber == randomnumber):
        print("Well done You knew the number :)")
        break
    
    if(hak == 0):
        print("Your right is over")
        break
