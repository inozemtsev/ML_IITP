import os, csv, numpy, pickle
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#Prepare data
datas=[]
with open ('data.csv', 'rb') as f:
    reader = csv.reader (f, delimiter='\n')
    for r in reader:
        datas.append (r)
data = []
for x in datas:
	data.append ([float(t) for t in x[0].split(',')])
data = numpy.array(data)

f = open ('training_data_new.pkl', 'r')
train_x, train_y = pickle.load (f)

#Training data visualization
pca = PCA (n_components = 2)
pca_res = pca.fit_transform (train_x)
selector1 = train_y == 'Rock'
selector2 = train_y == 'Pop'
selector3 = train_y == 'Jazz_Blues'
# print len ([y for y in train_y if y=='Jazz_Blues'])
plt.scatter(pca_res[selector1, 0], pca_res[selector1, 1], c='r')
plt.scatter(pca_res[selector2, 0], pca_res[selector2, 1], c='g')
plt.scatter(pca_res[selector3, 0], pca_res[selector3, 1], c='y')
plt.show()

#Given data
pca = PCA (n_components = 2)
pca_res = pca.fit_transform (data)
plt.scatter(pca_res[:, 0], pca_res[:, 1], c='r')
plt.show()

#Cross validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_x, train_y, test_size=0.4, random_state=0)
knn = KNN (n_neighbors=5, weights='distance')
knn.fit (X_train, y_train.T)
res = knn.predict (X_test)
print 'Errors: ', numpy.count_nonzero (res!=y_test), ' Elements: ', y_test.shape[0]

#Perform on test data
knn = KNN (n_neighbors=5, weights='distance')
knn.fit (train_x, train_y.T)
res = knn.predict (data)	
