def div(n):
	a = []
	for i in range(1,n+1):
		if n%i == 0:
			a.append(i)
	print("\n all of the divisors are:\n")
	for j in range(0,len(a)):
		print(a[j]," ")
	if j == 1 or j==0:
		print("this is prime")
	else:
		print("this is composite")
print("enter the number: \n")
num = int(input())
div(num)