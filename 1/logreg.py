import sklearn.datasets
import numpy as np
import matplotlib.pylab as plt

eps = 1e-1
step = 1e-3
def sigmoid_plus (w,x):
	return 1/(1+np.exp(-np.dot (w.T,x)))

def logreg (X,Y):
	X = np.hstack ((X,np.ones((len(X[:,:1]),1))))
	v = np.zeros ((3))
	v_add = np.sum ([(y-sigmoid_plus(v,x))*x for (x,y) in zip (X,Y)], axis = 0)
	while np.linalg.norm (v_add,2)>=eps:
		print v_add
		v+=step*v_add
		v_add = np.sum ([(y-sigmoid_plus(v,x))*x for (x,y) in zip (X,Y)], axis = 0)
	return [v[0],v[1],v[2]]	 



iris = sklearn.datasets.load_iris()
X = iris.data[:,:2]
Y = np.zeros (len(iris.target))
Y[iris.target > 0] = 1
Y[iris.target == 0] = 0
ans = logreg (X,Y)
a,b,c = ans[0], ans[1], ans[2]

iSelector = Y==0
plt.scatter(X[iSelector, 0], X[iSelector, 1], c='b')
plt.scatter(X[~iSelector, 0], X[~iSelector, 1], c='y')
plt.plot([1, 8], [(-a - c)/b , (-a*8 - c)/b])
plt.show()