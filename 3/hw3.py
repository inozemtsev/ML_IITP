import csv
import numpy as np
from sklearn import cross_validation

"""("id"), 0 - "latitude", 1 - "longitude", 2 - "summary",("description",)
"num_votes","num_comments","num_views",3 - "source",4 - "created_time", 
5 - "tag_type" """
data = []
with open ('train.csv', 'rb') as f:
    reader = csv.reader (f, delimiter=",")
    for r in reader:
        if r[0]=="id":
            continue
        data.append([])
        # data[-1].append (int(r[0]))
        data[-1].extend ([np.float64(x) for x in r[1:3]]) #coordinates
        data[-1].append (r[3]) #summary
        # data[-1].append(r[4])
        data[-1].extend ([np.int_(x) for x in r[5:8]]) #num_votes, num_comments, num_views
        data[-1].extend (r[8:]) #source, created_time, tag_type
data = np.array (data)
print data.shape
train_y = data[:,3:6]
train_x = np.delete (data, range(3,6), 1)
5BIBIL
import csv
import numpy as np

"""("id"), 0 - "latitude", 1 - "longitude", 2 - "summary",("description",)
"num_votes","num_comments","num_views",3 - "source",4 - "created_time", 
5 - "tag_type" """
train_x = []
train_y = []
with open ('train.csv', 'rb') as f:
    reader = csv.reader (f, delimiter=",")
    for r in reader:
        if r[0]=="id":
            continue
        train_x.append([])
        train_y.append([])
        # data[-1].append (int(r[0]))
        train_x[-1].extend ([np.float64(x) for x in r[1:3]]) #coordinates
        #data[-1].append (r[3]) #summary
        # data[-1].append(r[4])
        train_y[-1].extend ([np.int_(x) for x in r[5:8]]) #num_votes, num_comments, num_views
        #data[-1].extend (r[8:]) #source, created_time, tag_type
train_x = np.array (train_x)
train_y = np.array (train_y)

