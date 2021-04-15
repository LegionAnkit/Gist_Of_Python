# SIMPLE TRIANGLE PATTERN 
n=int(input("Enter the number of rows: "))
#NESTED FOR LOOP
for i in range(0,n):
	for j in range(0,i+1):
		print("* ",end="")
	print("\n")# WE USE PRINT TO CHANGE LINE IN THIS APPROACH

#ANOTHER WAY OF FOR NESTED LOOP

# for i in range(0,n): # Outer loop for rows
# 	star=""
# 	for j in range(0,i+1): # inner loop for columnns
# 		star+="* "
# 	print(star)	#WE DO NOT USE PRINT(\N) IN THIS APPROACH AS PRINT(STAR) CAGNGES LINE ITSELF IN EACH ITERATION

#THIS IS FOR LOOP
# for x in range(1,n+1):
# 	print("* " *x)


#THIS IS WHILE LOOP
# x=1
# while x<11:
# 	print("* "*x)
# 	x+=1

#THIS IS NESTED FOR AND WHILE LOOP 
# for x in range(1,11):
# 	count = 1
# 	star=""
# 	while count<=x:
# 		star+="* "
# 		count+=1
# 	print(star)
	