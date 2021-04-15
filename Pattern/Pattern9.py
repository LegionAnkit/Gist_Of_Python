#ALPHABETICAL PATTERN
n=int(input("Enter the number of rows: "))
num=65
for i in range(0,n):
	for j in range(1,i+2):
		ch=chr(num)
		print(f"{ch} ",end="")
	num+=1
	print("\n")