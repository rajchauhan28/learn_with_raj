import matrixexample
a = matrixexample.a3
b = matrixexample.b3
# Just imported matrix examples from the module already created

c = []
for i in range(len(a[1])):
	res = []
	for j in range(len(a)):
		print(a[i][j], b[i][j])
		# c[i][j] = a[i][j] + b[i][j]
		res.append( a[i][j] + b[i][j])
	c.append(res)
print(c)
print(a)