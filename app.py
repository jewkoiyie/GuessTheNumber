from random import randint
print("Hello the game begins\nPlease choose number between 0 and 20")
number = randint(0,20)
attempt = 3
def trying():
	try:
		global attempt
		userNumber = input("Nubmer: ")
		if int(userNumber) > number and attempt > 1:
			attempt = attempt - 1
			print("You have a " + str(attempt) + " attempts")
			print("Try a smaller number")
			trying()
		elif int(userNumber) < number and attempt > 1:
			attempt = attempt - 1
			print("You have a " + str(attempt) + " attempts")
			print("Try a bigger number")
			trying()
		elif int(userNumber) == number and attempt > 1:
			input("You win!")
		else:
			print("Game over\nThe number is ",number)
	except ValueError:
		print("ERROR. Try again please")
trying()
