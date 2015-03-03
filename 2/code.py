import numpy as np
a = [x for x in range(30) ]
for i in a:
	b = np.rand.randint() % 30
	if (b < 31):
		print b
		a[b] = 31
