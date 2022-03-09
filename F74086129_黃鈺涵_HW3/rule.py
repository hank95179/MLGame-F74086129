"""
The template of the script for playing the game in the ml mode
"""

class MLPlay:
	def __init__(self):
		"""
		Constructor
		"""
		pass
		self.onroad = False
		self.eat = False
	def update(self, scene_info):
		head = scene_info["snake_head"]
		snake = scene_info["snake_body"]
		tail = snake[len(snake)-1]
		body = scene_info["snake_body"][0]
		food = scene_info["food"]
		frame = scene_info["frame"]
		# print(frame)
		height = 0
		if(self.onroad == False):

			if head[1] != 290:
				return "DOWN"
			else:
				self.onroad = True
				height = food[1] / 10
				return "LEFT"
		# print(snake_head[0],snake_head[1])
		"""
		Generate the command according to the received scene information
		"""
		if scene_info["status"] == "GAME_OVER":
			print("frame: " ,frame)
			# print("head: " ,head)
			return "RESET"
		if(self.onroad):
			if head[0] == 0 and head[1] == 290:
				return "UP"
			elif frame > 25000:
				return "DOWN"
			elif head[0] == 0 and head[1] == 0:
				return "RIGHT"
			else:
				for i in range(15):
					if head[0] == 290 and head[1] == i * 20:
						return "DOWN"
					elif head[0] == 290 and head[1] == (i * 20) + 10:
						return "LEFT"
					elif head[0] == 10 and head[1] == (i * 20) - 10:
						return "DOWN"
					elif head[0] == 10 and head[1] == (i * 20) + 20:
						return "RIGHT"
				return "NONE"
			# print(food[1] - food[1] % 20)
			# if head[0] == 0:
			# 	height = food[1] / 20
			# if head[0] == 0 and head[1] == 0:
			# 	return "RIGHT"
			# # elif len(body) > 30:
			# # 	return "NONE"
			# elif  head[0] == 0 and head[1] != (food[1] - food[1] % 20):
			# 	return "UP"
			# elif head[0] == 0 and head[1] == (food[1] - food[1] % 20):
			# 	return "RIGHT"
			# elif head[0] != 0 and len(snake) < 10:
			# 	print(len(body))
			# 	for i in range(height,15):
			# 		if head[0] == 290 and head[1] == i * 20:
			# 			return "DOWN"
			# 		elif head[0] == 290 and head[1] == (i * 20) + 10:
			# 			return "LEFT"
			# 		elif head[0] == 10 and head[1] == (i * 20) - 10:
			# 			return "DOWN"
			# 		elif head[0] == 10 and head[1] == (i * 20) + 20:
			# 			return "RIGHT"
			# else: return "NONE"
		# if snake_head[0] > food[0]:
		# 	return "LEFT"
		# elif snake_head[0] < food[0]:
		# 	return "RIGHT"
		# elif snake_head[1] > food[1]:
		# 	return "UP"
		# elif snake_head[1] < food[1]:
		# 	return "DOWN"

	def reset(self):
		"""
		Reset the status if needed
		"""
		self.onroad = False
		self.eat = False
		pass
