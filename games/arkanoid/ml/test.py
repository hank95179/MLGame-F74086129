import random
class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.last_x = 0
        self.last_y = 0

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.

        x = scene_info["ball"][0]
        y = scene_info["ball"][1]
        temp = random.randint(1,20)
        plat = scene_info["platform"][0] +20
        vec_x = x - self.last_x
        vec_y = y - self.last_y
        if vec_x != 0:
         	vec_x /= abs(vec_x)
        command = "NONE"
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:        
	        if y > 335 and self.last_y > y:
	        	if x >= 175:
	        		command = "MOVE_LEFT"
	        	elif x <= 25:
	        		command = "MOVE_RIGHT"
	        	elif x > plat and plat <= 135 :
	        		command = "MOVE_RIGHT"
	        	elif x < plat and plat >= 70:
	        		command = "MOVE_LEFT"
	        elif self.last_y < y and y > 274:
	        	n = abs(395 - y)
	        	temp_x = x + vec_x * n
	        	if temp_x < 0:
	        		temp_x = abs(temp_x)
	        	if temp_x > 200:
	        		temp_x = 400 - temp_x
	        	if temp_x < 120 or temp_x > 80:
	        		if vec_x > 0 and plat < temp_x + 10:
	        			command = "MOVE_RIGHT"
	        		elif vec_x < 0 and plat > temp_x - 10:
	        			command = "MOVE_LEFT"
	        	elif temp_x > plat + temp :
	        		command = "MOVE_RIGHT"
	        	elif  temp_x < plat - temp:
	        		command = "MOVE_LEFT"
	        	else :
	        		command = "NONE"
	        elif y < 230 :
	        	if (temp % 2 == 0)  and plat > 75 and plat <125:
	        		command = "MOVE_LEFT"
	        	elif (temp % 2 == 1) and plat > 75 and plat <125:
	        		command = "MOVE_RIGHT"
                else:
                    command = "MOVE_RIGHT"                    
                elif plat > 100:
                    command = "MOVE_LEFT"
                else:
                    command = "MOVE_RIGHT"
        self.last_y = y
        self.last_x = x
        print(random.randint(1,20))
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False