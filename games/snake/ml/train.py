import pickle
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# beta 8.0.1
X_all = np.array([[0,0,0,0,0,0]])
y_all = np.array([])
j = 0
dir_path = '../log/'

all_file_list = os.listdir(dir_path)

for file in all_file_list:
    file_path = dir_path + file
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    scene_info_1P = data['scene_info']
    command_1P = data['command']

    k = range(1, len(scene_info_1P) - 1)
    head_x = np.array([scene_info_1P[i]['snake_head'][0] for i in k])
    head_y = np.array([scene_info_1P[i]['snake_head'][1] for i in k])
    food_x = np.array([scene_info_1P[i]['food'][0] for i in k])
    food_y = np.array([scene_info_1P[i]['food'][1] for i in k])    
    # tail_x = np.array([scene_info_1P[i]['snake_body'][len(scene_info_1P[i]['snake_body']) - 1][0] for i in k])
    # tail_y = np.array([scene_info_1P[i]['snake_body'][len(scene_info_1P[i]['snake_body']) - 1][1] for i in k])
    range_x = head_x - food_x   
    range_y = head_y - food_y
    # frame = np.array([scene_info_1P[i]['frame'] for i in k])
    # body = np.array(len([scene_info_1P[i]['snake_body'] for i in k]))
    target = np.where(np.array(command_1P) == 'NONE', 0,np.where(np.array(command_1P) == 'UP', 50,np.where(np.array(command_1P) == 'DOWN', 100 ,np.where(np.array(command_1P) == 'RIGHT',-50,-100))))[1:-1] 
    X_1P = np.hstack((
      head_x.reshape(-1, 1),
                   head_x.reshape(-1, 1),
                   food_x.reshape(-1, 1),
                   food_y.reshape(-1, 1),
                   range_x.reshape(-1, 1),
                   range_y.reshape(-1, 1)
                   # frame.reshape(-1, 1)
                   # tail_x.reshape(-1, 1),
                   # tail_y.reshape(-1, 1),
                   ))
    y_1P = target
    if (len(X_1P) == len(y_1P)):
        X_all = np.concatenate((X_all, X_1P))
        y_all = np.append(y_all, y_1P)
        j += 1

X_all = np.delete(X_all, 0, axis=0)

print(j)
model = KNeighborsClassifier(n_neighbors=5)
# model = GradientBoostingClassifier(learning_rate=1,max_depth=13)
print(model.fit(X_all, y_all))
print(model.score(X_all, y_all))
print(model.predict(X_all))

# In[30]:

with open('testDOU.pickle', 'wb') as f:
    pickle.dump(model, f)