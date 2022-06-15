import random
number= random.randint(1,10)

playername = input("Hello,What is your name?")
numberofguesses = 0
print("okay! "+playername+" I am choosing a number between 1 to 10 you have to guess it:")
print(number)
while numberofguesses < 5:
    guess= int(input())
    numberofguesses +=1
    if guess < number:
        print("Your guess was too low!")
    if guess > number:
        print("your guess was too high")
    if guess == number:
        break
if  guess == number:
    print("You have guessed it in "+str(numberofguesses)+" tries")
else :
    print("You have failed to guess in 5 guesses, the number was ", number)

