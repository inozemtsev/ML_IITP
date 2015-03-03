import sklearn.datasets
import numpy
import matplotlib.pyplot as plt

def badvector (X,Y,v):
    for i in range(len(X[:,:1])):
        if numpy.dot(v,X[i,:])*Y[i]<=0:
            return i

def perceptron (X,Y):
    X = numpy.hstack ((X,numpy.ones((len(X[:,:1]),1))))
    v = numpy.zeros ((1,3))
    bvnumber = badvector (X,Y,v)
    while (bvnumber != None):
        v+=Y[bvnumber]*X[bvnumber,:]
        bvnumber = badvector (X,Y,v)
    return [v[0][0], v[0][1], v[0][2]]

iris = sklearn.datasets.load_iris()
X = iris.data[:,:2]
Y = numpy.zeros (len(iris.target))
Y[iris.target != 0]=1
Y[iris.target == 0 ]=-1

ans = perceptron (X,Y)
a,b,c=ans[0],ans[1],ans[2]
    
iSelector = Y==-1
print type(iSelector)
plt.scatter(X[iSelector, 0], X[iSelector, 1], c='b')
plt.scatter(X[~iSelector, 0], X[~iSelector, 1], c='y')
plt.plot([4, 8], [(-a*4 - c)/b , (-a*8 - c)/b])
plt.show()