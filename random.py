import random
number = random.randint(1,9)
chance = 0
print ("Guess a number")
while(chance<5):
    guess = int(input("Enter your guess"))
    if guess == number:
        print ("Congratulations")
        break
    elif guess<number :
        print ("Too Low")
    else :
        print ("Too high")
    chance+=1
if chance >= 5 :
    print("You lost")    