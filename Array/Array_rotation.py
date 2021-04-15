import array as arr
a=arr.array('i',[])


length=int(input("enter the length of array: "))
print("Enter the elements in array: ",end=" ")
for x in range(0,length):
	ele=int(input())
	a.append(ele)

d=int(input("Enter the place from where rotation is to happen: "))

#Functoin to left rotate array of size n by d */
def arrayRotation(arr,d,n):
	print("Array before rotation: ", end=" ")
	for x in range(0,n): print(a[x],end=" ")

	print("\nArray after rotation: ",end=" ")
	for i in range(d):	#Left rotation by d
		temp=arr[0]	#Left rotation 
		for j in range(n-1): 
			arr[j]=arr[j+1]
		arr[n-1]=temp
	for x in range(n): print(arr[x],end=" ")		# print array

print(arrayRotation(a,d,length))