import array as arr  		#To import array as it is a module in python
a=arr.array('i',[])			#To create array here i means integer
length=int(input("Enter the length of Array: "))
print("Enter the element in Array:")
for x in range(0,length):
	ele=int(input())
	a.append(ele)

print(f"The array is :",end=" ")
max=a[0]
for i in range(0,length):
	print(a[i], end=" ")
	if a[i]>=max:
		max=a[i]
print(f"\nMax is {max}")

