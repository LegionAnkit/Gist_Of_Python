#NUMERICAL PATTERN
n=int(input("Enter the number of rows: "))
x=1
for i in range(0,n):
	for j in range(0,i+1):
		print(f"{x} ",end="")
		x+=1
	print("\n")