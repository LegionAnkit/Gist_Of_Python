		#USING SPACE OPTIMIZATION APPROACH

n=int(input("Enter the number to check in fibonacci series: "))


# a=0
# b=1
# c=0
# fib_series=[]
# fib_series.append(a)
# fib_series.append(b)
# while c<=n:
# 	c=a+b
# 	a=b
# 	b=c
# 	fib_series.append(c);
# if n in fib_series:
# 	print(f"{n} is a Fibonacci Number")
# else:
# 	print(f"{n} is not a Fibonacci Number")

		#USING THE FORMULA 

def isPerfectSquare(x):
	s=int(x**0.5)
	return s*s==x
def isFibonacciNo(num):
	return isPerfectSquare(5*num*num-4) or isPerfectSquare(5*num*num+4)
if isFibonacciNo(n)==True:
	print(f"{n} is a Fibonacci Number") 
else:
	print(f"{n} is not a Fibonacci Number")