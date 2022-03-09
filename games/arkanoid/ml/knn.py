"""
The template of the main script of the machine learning process
"""
import random
import os.path
import pickle

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        filename = 'arkanoid_n3_20210309_knn_model.pickle'
        filepath = os.path.join(os.path.dirname(__file__), filename)
        self.model = pickle.load(open(filepath, 'rb'))
        self.ball_served = False
        self.last_x = 0
        self.last_y = 0

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            nx = scene_info["ball"][0]
            ny = scene_info["ball"][1]
            px = scene_info["platform"][0]
            sx = nx - px
            sy = ny - 395
            x_speed = nx - self.last_x
            y_speed = ny - self.last_y
            if x_speed < 0:
                if y_speed < 0:
                    direct = 50
                else :direct = 100
            else:
                if y_speed < 0:
                    direct = 150
                else :direct = 200
            brick = len(scene_info["bricks"])
            command = self.model.predict([[nx, ny, px,direct]])
            # command = self.model.predict([[nx, ny, px,nx - self.last_x,ny - self.last_y]])
            self.last_x = nx
            self.last_y = ny
        if command == 0: return "NONE"
        elif command == 1: return "MOVE_LEFT"        
        else: return "MOVE_RIGHT"

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
