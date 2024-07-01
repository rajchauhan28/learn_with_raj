import matrixexample
a = matrixexample.a3
b = matrixexample.b3
c= []
for i in range(len(a)):
	res = []
	for j in range(len(b[0])):
		sum = 0
		for k in range(len(b)):
			sum += a[i][k]*b[k][j]
		res.append(sum)
	c.append(res)

for i in c:
	print(i)
