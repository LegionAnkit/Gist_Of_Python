given_number=input("Enter a number to check whether it is Armstrong Number: ")
length=len(given_number)
number=int(given_number)
clone_num=number
if clone_num>0:	
	storage=0
	while clone_num!=0:
		digit=clone_num%10		
		clone_num=clone_num//10
		storage=(digit**length)+storage
	if number==storage:
		print(f"The given number {number} is Armstrong Number")
	else:
		print(f"The given number {number} is not Armstrong Number")
else:
	print("Enter a positive integer...!!")
