import matrixexample

a = matrixexample.a4

print(list(zip(*a)))
# or numpy

import numpy
print(numpy.transpose(a))

# for loop
c = []
for j in range(len(a[0])):
	res = []
	for i in range(len(a)):
		res.append(a[i][j])
	c.append(res)
print(c)

