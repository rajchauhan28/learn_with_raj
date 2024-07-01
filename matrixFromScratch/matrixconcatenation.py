import matrixexample

a = matrixexample.a4
b = matrixexample.b4
c = []
for i in range(len(a)): # rows
	res = []
	for j in range(len(a[0])): # columns
		res.append(a[i][j]+b[i][j])
		print(a[i][j]+b[i][j])
	c.append(res)

print(c)