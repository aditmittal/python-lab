import math

f1 = open('file1.txt','w')
f2 = open('file2.txt','w')
f3 = open('file3.txt','w')

s1 = input("enter the string 1")
f1.write(s1)
f1.close()

s2 = input("enter the string 2")
f2.write(s2)
f2.close()

f1 = open('file1.txt','r')
f2 = open('file2.txt','r')
f1r = f1.read()
f2r = f2.read()
print("\n contents of first file are: "+f1r)
print("contents of second file are: "+f2r)
f1words = f1r.split(' ')
f2words = f2r.split(' ')
f3words = []

len1 = len(f1words)
len2 = len(f2words)

if len1>len2:
    big = len1
else:
    big = len2
for i in range (0,big):
    half1 = ''
    half2 = ''
    if i<len1:
        half1 = half1 + f1words[i][0:math.ceil(len(f1words[i])/2)]
    if i<len2:
        half2 = half2 + f2words[i][0:math.ceil(len(f2words[i])/2)]
    f3words.append(half1 + half2)
f3words = ' '.join(f3words)
f3.write(f3words)
f3 = open('file3.txt','r')
print("\n content of 3rd file is: "+f3.read())
