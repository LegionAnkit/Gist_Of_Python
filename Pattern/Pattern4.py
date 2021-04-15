#CENTERED TRIANGLE PATTERN
n= int(input("Enter the number of rows: "))
space=n
for i in range(0,n):
	for j in range(space,1,-1):
		print(" ",end="")
	for k in range(0,i+1):
		print("* ",end="") 
	space-=1
	print("\n")

#ANOTHER APPROACH

# spc=n
# for i in range(0,n):
# 	space=""
# 	star=""
# 	for j in range(spc,1,-1):
# 		space+=" "
# 	for k in range(0,i+1):
# 		star+="* "
# 	spc-=1
# 	print(f"{space}{star}")