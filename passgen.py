import random
import string

str = string.ascii_letters + string.digits + string.punctuation

l = int(input("enter length of password: "))
for i in range(l):
	print((random.choice(str)),end = '')

