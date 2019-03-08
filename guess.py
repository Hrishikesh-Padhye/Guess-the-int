import random
import time

def welcome():
	global playername
	playername = input("Hello! May I know your name? :) \n")
	reply1 = input("Hey "+playername+"! How are you doing ? \n")
	reply2 = input("Would you like to play a game with me ? \n")
	if reply2 in ["n","N","no","No","NO"]:
		print("Okay then goodbye \n")
		exit()
	print("Okay then lets play a game!! \n")	
	print(''' Here is the thing - 
	I have an integer between 1 and your difficulty level in my mind
	Your task is to guess that number in as few attempts as possible within 6 attempts''')
	i = 5
	print("Your game begins in ")
	while i != 0:
		print(str(i)+"...")
		i = i-1 
		time.sleep(1)

def game():
	global playername
	difficulty = input("Set your difficulty level (1-100) -> ")
	difficulty = int(difficulty)
	number = random.randint(1,difficulty)
	totalguesses = 0
	while totalguesses<6:
		print("What is your guess?")
		guess = input()
		totalguesses = totalguesses + 1
		try:
			guess=int(guess)
		except:	
			print("You are supposed to make an integer guess!") 
			totalguesses = totalguesses -1
			continue
		if guess < number:
			print("Too low ! You have "+ str(6 - totalguesses) +" guesses left")
		elif guess > number:
			print("Too high ! You have "+ str(6 - totalguesses) +" guesses left")
		elif guess == number:
			print("Bingooo!! You're so good at this game! Good guessing "+	playername)
			break	
	if guess != number:
		number = str(number)				
		print("I am sorry mate, the number I was looking for was " + number )    		

if __name__ == "__main__":
	playername = ''
	welcome()
	game()
	while True:
		print("Do you wish to play again?")		
		again = input()
		if again in ["n","N","no","No","NO","nope","nah"]:
			print("Okay then goodbye \n")
			exit()
		print("Okay! Here we go again")
		time.sleep(2)
		game()


