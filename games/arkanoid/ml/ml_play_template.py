"""
The template of the main script of the machine learning process
"""
import random
class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.last_x = 0
        self.last_y = 0
        self.move = 0
        self.set = 16 
        self.m = random.randint(1,16)
    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.

        x = scene_info["ball"][0]
        y = scene_info["ball"][1]
        temp = random.randint(1,14)
        plat = scene_info["platform"][0] +20
        if(plat == 180 or plat == 20):
            self.m = temp
        vec_x = x - self.last_x
        vec_y = y - self.last_y
        if vec_x != 0 and vec_y != 0:
            vec_x /= abs(vec_y)
        command = "NONE"
        if (scene_info["status"] == "GAME_PASS" or scene_info["status"] == "GAME_OVER"):
            self.move = 0;
            self.set -= 2
            return "RESET"

        if not self.ball_served:
            if self.move != self.set:
                command = "MOVE_RIGHT"
                self.move += 1
            else:
                command = "SERVE_TO_LEFT"
                self.ball_served = True
        else:        
            # if y > 350 and self.last_y > y:
            #     if x >= 175:
            #         command = "MOVE_LEFT"
            #     elif x <= 25:
            #         command = "MOVE_RIGHT"
            #     if x > plat and plat <= 135 :
            #         command = "MOVE_RIGHT"
            #     elif x < plat and plat >= 70:
            #         command = "MOVE_LEFT"
            # if  y > 390 and y < 100:
            #     command = "NONE"     
            if self.last_y < y :
                n = abs(395 - y)
                temp_x = x + vec_x * n
                if temp_x < -200:
                    temp_x = 400 - abs(temp_x)
                if temp_x < 0:
                    temp_x = abs(temp_x)
                if temp_x > 200:
                    temp_x = 400 - temp_x                 
                # if temp_x < 125 or temp_x > 75:
                #     if vec_x > 0 and plat < temp_x + temp:
                #         command = "MOVE_RIGHT"
                #     elif vec_x < 0 and plat > temp_x - temp:
                #         command = "MOVE_LEFT"
                # if temp % 2 == 0:
                #     if temp_x + temp > plat:
                #         command = "MOVE_RIGHT"
                #     elif temp_x + temp < plat:
                #         command = "MOVE_LEFT"
                # elif temp_x + temp> 200  :
                #     x = 400 - temp_x - temp
                #     if plat > x:
                #         command = "MOVE_LEFT"
                #     elif plat < temp_x + temp:
                #         command = "MOVE_LEFT"
                else:
                    if  temp_x   < plat - 15:
                        command = "MOVE_LEFT"
                    elif  temp_x  > plat + 15:
                        command = "MOVE_RIGHT"
                    else:command = "NONE"
                # elif  temp_x - temp < 0 :
                #     if plat > abs(temp_x - temp):
                #         command = "MOVE_LEFT"
                #     elif plat < temp_x + temp:
                #         command = "MOVE_LEFT"
                # print(temp_x)
            else:
                if plat > 100:
                    command = "MOVE_LEFT"
                elif plat < 100:
                    command = "MOVE_RIGHT"

        self.last_y = y
        self.last_x = x
        self.last_b = plat   
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
