li = "brontosaurus"
di = {}
for i in li:
	
		if i in di:
			di[i] = di[i] + 1
		else:
			di[i]  = 1
print(di)