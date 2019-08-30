def linfunc(a,k):
	for i in range(0,len(a)):
		if k == a[i]:
			return True
			break
	return False

a=[]
print("enter number of elements")
n = int(input("\nhere"))
k=int(input("enter k here"))
print("enter array")
for j in range (0,n):
	a.append(int(input()))

bh = linfunc(a,k)
print("statement that ",k," is in list is :",bh)