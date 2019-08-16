n = int(input("enter till which number you want the list: "))
li = []
li.append(1)
li.append(1)
for i in range (2,n):
	li.append( li[i-1] + li[i-2])
print("the following series is")
for j in range (0,n):
	print(li[j])
