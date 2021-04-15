#NUMERICAL PATTERN
n=int(input("Enter the number of rows: "))

for i in range(0,n):
	for j in range(1,i+2):
		print(f"{j} ",end="")
	print("\n")