def revstr(a):
	w = a.split()
	w.reverse()
	str = ' '.join(w)
	print("rev by words: ",str)
	print("rev by char and word: ",a[::-1])
	print("reversed by char not words",str[::-1])

s = input("enter string of words: ")
revstr(s)
