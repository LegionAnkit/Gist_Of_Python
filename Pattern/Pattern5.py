#TRIANGLE (ISOSCELES)
n= int(input("Enter the number of rows: "))
space=n
for i in range(0,n):
	for j in range(space,1,-1):
		print(" ",end="")
	for k in range(0,i+1):
		print("*",end="")
	for x in range(0,i):
		print("*",end="")
	space-=1
	print("\n")