di = {"chuck":1,"annie":42,"jane":200,"bhand":420}
print("\nsort by keys \n")
for k in sorted(di.keys()):
	print(k + " :: "+str( di[k]))
print("\n\nsorted by value\n")
ndi = {}
for k,val in di.items():
	ndi[val] = k
for a in sorted(ndi.keys()):
	print(str(a) + " :: "+str(ndi[a]))