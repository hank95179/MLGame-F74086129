"""
The template of the script for playing the game in the ml mode
"""
import os
import pickle

import numpy as np

class MLPlay:
	def __init__(self):
		"""
		Constructor
		"""
		pass
		self.onroad = False
		self.eat = False
		with open(os.path.join(os.path.dirname(__file__), 'testDOU.pickle'), 'rb') as f:
			self.model_1P = pickle.load(f)
	def update(self, scene_info):
		head = scene_info["snake_head"]
		snake = scene_info["snake_body"]
		tail = snake[len(snake)-1]
		body = scene_info["snake_body"][0]
		food = scene_info["food"]
		frame = scene_info["frame"]
		height = 0
		
		# print(snake_head[0],snake_head[1])
		"""
		Generate the command according to the received scene information
		"""
		if scene_info["status"] == "GAME_OVER":
			print("frame: " ,frame)
			# print("head: " ,head)
			return "RESET"
		else:
			head_x = head[0] 
			head_y = head[1]
			food_x = food[0]
			food_y = head[1]
			tail_x = tail[0]
			tail_y = tail[1]
			range_x = head_x - food_x		
			range_y = head_y - food_y		
			x = np.array([head_x,head_y,food_x,food_y,range_x,range_y])	.reshape((1, -1))
			y = self.model_1P.predict(x)
			# print(y)
			if y == 0:
				return "NONE"
			elif y == 50:
				return "UP"
			elif y == 100:
				return "DOWN"
			elif y == -100:
				return "LEFT"
			elif y == -50:
				return "RIGHT"
	def reset(self):
		"""
		Reset the status if needed
		"""
		self.onroad = False
		self.eat = False
