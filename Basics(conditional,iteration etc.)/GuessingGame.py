from random import randint
random_no=randint(1,10)
while True: #Iterates endlessly untill break
	guessed_no=int(input("Guess a number from 1-10:"))
	if guessed_no<random_no:
		print("Too Low..! try again !\n")
	elif guessed_no>random_no:
		print("To High...! try again..!!\n")
	else:
		print("You Won ...!!\n")
		ch=input("Do you want to play again (y/n):\n")
		if ch=="y":
			random_no=randint(1,10)
			guessed_no=None
		else:
			print("Thank You for playing ..!!")
			break


