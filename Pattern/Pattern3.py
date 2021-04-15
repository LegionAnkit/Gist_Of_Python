# RIGHT SIDE TRIANGLE PATTERN WITH A SINGLE SPACE IN BETWEEN *

# NESTED FOR USING end keyword of print function

n= int(input("Enter the number of rows: "))
space=n*2
for i in range(0,n):
	for j in range(space,2,-1):
		print(" ",end="")
	for k in range(0,i+1):
		print("* ",end="")
	space-=2
	print("\n")

#ANOTHER APPROACH
# spc=n*2
# for i in range(0,n):
# 	space=""
# 	star=""
# 	for j in range(spc,2,-1):
# 		space+=" "
# 	for k in range(0,i+1):
# 		star+="* "
# 	spc-=2
# 	print(f"{space}{star}")