#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pickle
import numpy as np
import os
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# beta 8.0.1
X_all = np.array([[0, 0, 0, 0]])
y_all = np.array([])
j = 0
dir_path = '../logs/'

all_file_list = os.listdir(dir_path)

for file in all_file_list:
    file_path = dir_path + file
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    scene_info_1P = data['ml']['scene_info']
    command_1P = data['ml']['command']

    k = range(1, len(scene_info_1P) - 1)
    x = np.array([scene_info_1P[i]['ball'][0] for i in k])
    y = np.array([scene_info_1P[i]['ball'][1] for i in k])
    P1_X = np.array([scene_info_1P[i]['platform'][0] for i in k])
    frame = np.array([scene_info_1P[i]['frame'] for i in k])
    target = np.where(np.array(command_1P) == 'NONE', 0,
                          np.where(np.array(command_1P) == 'MOVE_LEFT', -1, 1))[1:-1]  # [0] SERVE_TO_RIGHT, [1897] None
    X_1P = np.hstack((x.reshape(-1, 1),
                   y.reshape(-1, 1),
                   # xs.reshape(-1, 1),
                   # ys.reshape(-1, 1),
                   P1_X.reshape(-1, 1),
                   # P2_X.reshape(-1, 1),
                   frame.reshape(-1,1)
                   ))
    y_1P = target
    if (len(X_1P) == len(y_1P)):
        X_all = np.concatenate((X_all, X_1P))
        y_all = np.append(y_all, y_1P)
        j += 1

X_all = np.delete(X_all, 0, axis=0)

print(j)
# model = KNeighborsClassifier(n_neighbors=3)
model = GradientBoostingClassifier(learning_rate=1,max_depth=13)
print(model.fit(X_all, y_all))
print(model.score(X_all, y_all))

# In[30]:

with open('GBC.pickle', 'wb') as f:
    pickle.dump(model, f)
