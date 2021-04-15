n=int(input("Enter the number of terms for Fibonacci Series: "))
if n<0:
	print("Incorrect Input")
a=0
b=1
fib_series=[]
fib_series.append(a)
fib_series.append(b)
for x in range(0,n-2):
	c=a+b
	a=b
	b=c
	fib_series.append(c)
print(fib_series)

# Alternate method using Func

# def fib_list(max):
# 	fib = []
# 	a, b = 0, 1
# 	while len(fib)<max:
# 		fib.append(b)
# 		a, b= b, a+b
# 	return fib
	

