# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#load the result.txt gotten from reduce program
file = open('result.txt')

#build the similarity matrix using the candidate pair in result.txt
sim_matrix=np.zeros((3000,3000))
for line in file:
    line = line.strip()
    
    result = line
    result = result.replace('[','')
    result = result.replace(']','')
    result = result.replace('\'','')
    result = result.replace(' ','')
    result = result.split(',')
    result.pop(0)
    
    if len(result) == 1:
        continue
    else:
        result=map(int,result)
        for row in result:
            for column in result:
                sim_matrix[row-1,column-1]=1

#construct the training data matrix, create I,pred matrix
train_data = pd.read_csv('train.txt', sep='\t', header=None)
n_users = max(np.unique(train_data [0]))
n_items = max(np.unique(train_data [1]))

train_data_matrix = np.zeros((n_users, n_items))
I = np.ones((n_users, n_items))
pred=np.zeros((n_users, n_items))
for line in train_data.itertuples():
    train_data_matrix[line[1]-1, line[2]-1] = line[3]  
    I[line[1]-1, line[2]-1] = 0

#using similarity matrix to predict value
for user in range(3000):
    s=sum(sim_matrix[user,:])
    #s cannot equal 0, because it is used as a denominator
    if s!=0:
        for movie in range(11893):
            pred[user,movie]=sim_matrix[user,:].dot(train_data_matrix[:,movie])/s
            print(str(user),str(movie))
    else:
        continue

#using I matrix to add the true value back
prediction=np.zeros((n_users, n_items))
prediction=pred*I+train_data_matrix 

#calculate RMSE
from sklearn.metrics import mean_squared_error
from math import sqrt
test_data = pd.read_csv('test.txt', sep='\t', header=None)
ground_truth=[]
user_result=[]
for line in test_data.itertuples():
    ground_truth.append(line[3])
    user_result.append(prediction[line[1]-1,line[2]-1])

rmse_user=sqrt(mean_squared_error(ground_truth, user_result))
print ('LSH RMSE: ' + str(rmse_user))