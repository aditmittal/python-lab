def evlist(li):
    l2 = []
    for i in range (0,len(li)):
        if(li[i]%2==0):
            l2.append(li[i])
    print("the list of even numbers is")
    for j in range(0,len(l2)):
        print(l2[j])

print("input list one")
li = []
n = int(input("enter number of elements"))
for i in range(0,n):
    a = int(input("enter number"))
    li.append(a);
evlist(li)
