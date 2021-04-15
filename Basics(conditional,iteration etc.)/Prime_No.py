a=int(input("Enter the staring number:  "))
b=int(input("Enter the last number:  "))
for num in range(a,b+1):  	#The interval bet numbers
	temp=0
	if num>1:
		for x in range(2,num):		# To find Prime No
			if num%x==0:
				temp+=1
		if temp>0:
			print(num,"is not a Prime No")
		else:
			print(num,"is a Prime No")
	else:
		print(num,"is a Prime No")

				#To only find Prime No

# if num>1:
# 	for x in range(2,num):
# 		if num%x==0:
# 			temp+=1
# 	if temp>0:
# 		print(num,"is not a Prime No")
# 	else:
# 		print(num,"is a Prime No")
# else:
# 	print(num,"is a Prime No")