#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pickle
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# beta 8.0.1
X_all = np.array([[0, 0, 0, 0, 0, 0]])
y_all = np.array([])
j = 0
dir_path = '../log39/'

all_file_list = os.listdir(dir_path)

for file in all_file_list:
    file_path = dir_path + file
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    scene_info_2P = data['ml_2P']['scene_info']
    scene_info_1P = data['ml_1P']['scene_info']
    command_2P = data['ml_2P']['command']

    k = range(1, len(scene_info_2P) - 1)  # 為了取一筆data的每一個frame info:
    x = np.array([scene_info_2P[i]['ball'][0] for i in k])
    y = np.array([scene_info_2P[i]['ball'][1] for i in k])
    xs = np.array([scene_info_2P[i + 1]['ball_speed'][0] for i in k])
    ys = np.array([scene_info_2P[i + 1]['ball_speed'][1] for i in k])
    P1_X = np.array([scene_info_2P[i]['platform_1P'][0] for i in k])
    P2_X = np.array([scene_info_2P[i]['platform_2P'][0] for i in k])
    blocker = np.array([scene_info_2P[i]['blocker'][0] for i in k])
    target = np.where(np.array(command_2P) == 'NONE', 0,
                          np.where(np.array(command_2P) == 'MOVE_LEFT', -1, 1))[1:-1]  # [0] SERVE_TO_RIGHT, [1897] None
    X_2P = np.hstack((x.reshape(-1, 1),
                   y.reshape(-1, 1),
                   xs.reshape(-1, 1),
                   ys.reshape(-1, 1),
                   P1_X.reshape(-1, 1),
                   P2_X.reshape(-1, 1),
                   ))
    y_2P = target
    if(len(X_2P) == len(y_2P)):
        X_all = np.concatenate((X_all, X_2P))
        y_all = np.append(y_all, y_2P)
        j += 1

X_all = np.delete(X_all, 0, axis=0)
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
model = KNeighborsClassifier(n_neighbors=3)
print(model.fit(X_all, y_all))
print(model.score(X_all, y_all))
print(j)
# In[30]:

with open('2P700.pickle', 'wb') as f:
    pickle.dump(model, f)