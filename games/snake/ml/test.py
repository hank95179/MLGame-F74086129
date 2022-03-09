"""
The template of the script for playing the game in the ml mode
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        pass

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER":
            return "RESET"

        head = scene_info["snake_head"]
        food = scene_info["food"]
        body = scene_info["snake_body"]
        tail = body[len(body)-1]
        bftail = body[len(body)-2]
        tail_velocity = [(tail[0] - bftail[0]),(tail[1] - bftail[1])]
        # print(tail_velocity)
        left = True
        right = True
        up = True
        down = True
        body_x = 0
        body_y = 0
        if (head[0] > 280 or head[0] == 0) and not_at_limit(body[0][0],body[0][1]):
            if head[1] > food[1]:
                return "UP"
            else:return "DOWN" 
        if (head[1] > 280 or head[1] == 0) and not_at_limit(body[0][0],body[0][1]):
            if head[0] > food[0]:
                return "LEFT"
            else:return "RIGHT" 
        for i in range(len(body)):
            if((head[0]-10 == body[i][0] and head[1] == body[i][1]) or head[0] == 0):
                left = False
            elif((head[0]+10 == body[i][0] and head[1] == body[i][1]) or head[0] == 290):
                right = False
            elif((head[1]-10 == body[i][1] and head[0] == body[i][0]) or head[1] == 0):
                up = False
            elif((head[1]+10 == body[i][1] and head[0] == body[i][0]) or head[1] == 290):
                down = False 
        if head[0] > food[0]:
            # print("上",up,"下",down,"左",left,"右",right)
            if left == True:
                return "LEFT"
            elif up == True and tail_velocity[1] == -10:
                return "UP"
            elif down ==True:
                return "DOWN"
            elif right ==True:
                return "RIGHT"
            else:return "UP"
        elif head[0] < food[0]:
            # print("上",up,"下",down,"左",left,"右",right)
            if right == True:
                return "RIGHT"
            elif down ==True and tail_velocity[1] == 10:
                return "DOWN"
            elif up == True:
                return "UP"
            elif left ==True:
                return "LEFT"
            else:return "DOWN"
        elif head[1] > food[1]:
            # print("上",up,"下",down,"左",left,"右",right)
            if up == True:
                return "UP"
            elif right ==True and tail_velocity[0] == -10:
                return "RIGHT"
            elif left == True:
                return "LEFT"
            elif down ==True:
                return "DOWN"
            else:return "RIGHT"
        elif head[1] < food[1]:
            # print("上",up,"下",down,"左",left,"右",right)
            if down == True:
                return "DOWN"
            elif right ==True and tail_velocity[0] == 10:
                return "RIGHT"
            elif left == True:
                return "LEFT"
            elif up ==True:
                return "UP"
            else:return "RIGHT"

    def reset(self):
        """
        Reset the status if needed
        """
        pass
def not_at_limit(a,b):
    if a != 0 and a != 290 and b != 0 and b != 290:
        return True
    else:return False