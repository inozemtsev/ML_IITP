
# coding: utf-8

# In[1]:

import sklearn.datasets
import numpy
import matplotlib.pylab as plt


# In[3]:

## Формирование датасета (X, Y)
iris = sklearn.datasets.load_iris()
X = iris.data[:, :2]
Y = numpy.zeros(len(iris.target))
Y[iris.target>0] = 1


# In[4]:

## Визуализация
iSelector = Y==0
plt.scatter(X[iSelector, 0], X[iSelector, 1], c='b')
plt.scatter(X[~iSelector, 0], X[~iSelector, 1], c='y')
plt.show()


# In[5]:

## Обучение персептрона
from sklearn.linear_model import Perceptron
model = Perceptron(n_iter=200)
model.fit(X, Y)
# вытаскиваем коэффициенты из модели
a = model.coef_[0][0]
b = model.coef_[0][1]
c = model.intercept_[0]

## Здесь дожен быть вызов вашей функции, которая по данным ей (X,Y) вернет коэффициенты a,b,c 
## (считаем, что у нас двухмерное исходное признаковое пространство и задача бинарной классификации)


# In[7]:

## Отрисовка результата
iSelector = Y==0
plt.scatter(X[iSelector, 0], X[iSelector, 1], c='b')
plt.scatter(X[~iSelector, 0], X[~iSelector, 1], c='y')
# рисуем по ним прямую
plt.plot([4, 8], [(-a*4 - c)/b , (-a*8 - c)/b])
plt.show()


# In[14]:

a = numpy.concatenate((numpy.ones(5), numpy.zeros(5)))


# In[17]:

a + arange(10)


# In[11]:

a

