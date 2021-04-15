	#USING SPACE OPTIMIZATION APPROACH

def nth_fibonacci(n):
	a=0
	b=1
	if n<1:
		return print("Incorrect input..!")
	elif n==1:
		return a
	elif n==2:
		return b
	else:
		for x in range(1,num-1):
			c=a+b
			a=b
			b=c
		return c
num=int(input("Enter the nth term of fibonacci series: "))
print(f"The {num} term of Fibonnaci Series is {nth_fibonacci(num)}")

	# USING DYNAMIC PROGRAMMING APPROACH

# FibArray=[0,1]
# def fib(n):
# 	if n<0:
# 		print("Incorrect input..")
# 	elif n<=len(FibArray):
# 		return FibArray[n-1]
# 	else:
# 		temp_fib=fib(n-1)+fib(n-2)
# 		FibArray.append(temp_fib)
# 		return temp_fib
# print(fib(9))
