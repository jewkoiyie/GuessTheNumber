import random
print("Hello the game begins")
number = random.randint(0,20)
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
			print("Game over")
	except ValueError:
		input("ERROR. Try again please")
trying()