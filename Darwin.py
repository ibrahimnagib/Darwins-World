#Darwin.py

#allthree.py
import random

class Darwin:
	def __init__(self, x_axis, y_axis):
		self.x_axis = int(x_axis)
		self.y_axis = int(y_axis)
		self.species_list = []
		self.direction_list = []
		self.creature_list = []

		empty = Species(".")
		wall = Species("*")


		self.board = [[empty for i in range(y_axis+2)] for j in range(x_axis+2)]
		
		for t in range(y_axis+2):
			self.board[0][t] = wall
			self.board[-1][t] = wall
		for l in range(x_axis+2):
			self.board[l][0] = wall
			self.board[l][-1] = wall
		


	def place_creature(self, creature, start_x, start_y, direction): 
		self.board[(start_x+1)][start_y+1] = creature.species
		creature.direction = direction
		creature.xcord = start_x+1
		creature.ycord = start_y+1

		self.creature_list.append(creature)
		self.direction_list.append(direction)

		
	def update_creature(self, c_index, s):
		self.creature_list[c_index].species = s


	# def if_wall(self, space_ahead, c_index):
	# 	if space_ahead == wall:
	# 		return True
	# 	else:
	# 		return False
	# 	#print("wall")

	def if_empty(self, space_ahead, c_index):
		empty = Species(".")
		#print ("if_empty")
		# print("empty: ",empty)
		# print("space: ",space_ahead)
		if space_ahead.name == empty.name:
			#print("true")
			return True

		else:
			return False
		

	def if_random(self, space_ahead, c_index):
		if random.randrange(0,2) % 2 == 0:
		 	return True
		else:
			return False
		#print("if_random")

	def go(self, space_ahead, c_index):
		#print('go')
		return True

		

	def if_enemy(self, space_ahead, c_index):
		#print("if_enemy")
		empty = Species(".")
		wall = Species("*")
		s = self.creature_list[c_index].species
		if space_ahead.name == empty.name:
			return False

		elif space_ahead.name == wall.name:
			return False

		elif space_ahead.name == s.name:
			return False


				#print("true")
		else:
				#print("fasle")
			return True
		# #print("if_enemy")
		# empty = Species(".")
		# s = self.creature_list[c_index].species
		# if space_ahead.name == empty.name:
  #           return False

  #       elif space_ahead.name == s.name:
		# 	return False
		# 		#print("true")
		# else:
		# 		#print("fasle")
		# 	return True

	def infect(self, space_ahead, c_index):
		s = self.creature_list[c_index].species
		for x in self.creature_list:
			if x.xcord == space_ahead.x and x.ycord == space_ahead.y:
				x.species = s
				
		# x = space_ahead.x
		# y = space_ahead.y
		# direction = self.creature_list[c_index].direction
		# new_creature = Creature(s)
		# self.place_creature(new_creature, x, y, direction)
		#print("infect")

	def left (self, space_ahead, c_index):
		#c = self.creature_list[c_index]
		if self.creature_list[c_index].direction == "north":
			self.creature_list[c_index].direction = "west"
			return
		if self.creature_list[c_index].direction == "west": 
			self.creature_list[c_index].direction = "south"
			return
		if self.creature_list[c_index].direction == "south":
			self.creature_list[c_index].direction = "east" 
			return
		if self.creature_list[c_index].direction == "east": 
			self.creature_list[c_index].direction = "north"
			return

		#print("left")
	def right (self, space_ahead, c_index): 
		#c = self.creature_list[c_index]
		if self.creature_list[c_index].direction == "north":
			self.creature_list[c_index].direction = "east"
			return
		if self.creature_list[c_index].direction == "west": 
			self.creature_list[c_index].direction = "north"
			return
		if self.creature_list[c_index].direction == "south":
			self.creature_list[c_index].direction = "west" 
			return
		if self.creature_list[c_index].direction == "east": 
			self.creature_list[c_index].direction = "south"
			return
	
			
		#print("right")

	def hop(self, space_ahead, c_index):
		print("hop ",c_index)
		if self.if_empty(space_ahead, c_index)!=True:
			return
		else: 
			empty = Species(".")
			c = self.creature_list[c_index]
			self.board[c.xcord][c.ycord] = empty
# 
# 
	 	if c.direction == "north":
 			c.xcord -= 1
 		if c.direction == "south":
			c.xcord += 1
		if c.direction == "west":
			c.ycord -= 1
		if c.direction == "east":
 		 	c.ycord += 1
		self.board[c.xcord][c.ycord] = c.species
		#Darwin.update_creature(self.xcord,self.ycord,self.direction)

	def play_round(self, space_ahead, c_index):
		j = 0
		s = self.creature_list[c_index].species
		for i in range(len(s.instruction_list)):
			if i != j:
				continue
			r = s.instruction_list[i] 
			if " " in r:
				r = r.split(" ")
				command = getattr(Darwin, r[0])
				#print(command)
				if command(self, space_ahead, c_index) == True:
					j = int(r[1])
					#print(j)
					if j == 0:
						break
					continue
			else:
				command = getattr(Darwin, r)
				command(self,space_ahead, c_index)
			j+=1


	def show_board(self):
		for s in self.board:
			print " ".join(x.symbol for x in s)
			#print(s.split())
		#print(self.board)

	def run(self,n):
		x = 0
		y = 0
		for i in range(n):
			for j in range(len(self.creature_list)):
				if self.direction_list[j] == "north":
					y = self.creature_list[j].xcord -1
					#print("y: ", y)
					x = self.creature_list[j].ycord
				elif self.direction_list[j] == "south":
					y = self.creature_list[j].xcord + 1
					x = self.creature_list[j].ycord
				elif self.direction_list[j] == "west":
					y = self.creature_list[j].xcord
					x = self.creature_list[j].ycord -1
				elif self.direction_list[j] == "east":
					y = self.creature_list[j].xcord
					x = self.creature_list[j].ycord + 1

				temp_s = self.board[x][y]
				self.play_round(temp_s, j)
				#print("temp_s: ", temp_s)
				print("Round: ", i, j)
				self.show_board()


				
				#self.update_creature(j,creature.g)


	def __remove_creature(self, creature, space_ahead):
		self.creature_list.remove(creature)
		self.board[creature.xcord][creature.ycord] = Species(".")
		self.direction_list.remove(creature.direction)



class Species:
	def __init__(self,name):
		self.name = name
		self.symbol = name[0]
		self.instruction_list = []
		self.x = 0
		self.y = 0

	def __str__(self):
		return self.name

	# def set_xy(self,x,y):
	# 	self.x = x
	# 	self.y = y

	# def get_xy(self):
	# 	return self.x, self.y
		
	def add_instruction(self, instruction):
		self.instruction_list.append(instruction)



class Creature:
	def __init__(self, species):
		self.species = species
		#self.species.set_xy(xcord,ycord)
		self.direction = ''
		self.xcord = 0
		self.ycord = 0
		self.counter = 0

	def __str__(self):
		return self.species

