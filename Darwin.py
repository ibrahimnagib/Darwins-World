# Darwin.py

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

        self.board = [[empty for i in range(y_axis + 2)] for j in range(x_axis + 2)]

        for t in range(y_axis + 2):
            self.board[0][t] = wall
            self.board[-1][t] = wall
        for l in range(x_axis + 2):
            self.board[l][0] = wall
            self.board[l][-1] = wall


    def place_creature(self, creature, start_x, start_y, direction):
        self.board[(start_x + 1)][start_y + 1] = creature.species
        creature.direction = direction
        creature.xcord = start_x + 1
        creature.ycord = start_y + 1

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
        if random.randrange(0, 2) % 2 == 0:
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
                return

    def left(self, space_ahead, c_index):
        c = self.creature_list[c_index]
        if c.direction == "north":
            c.direction = "west"
            return
        if c.direction == "west":
            c.direction = "south"
            return
        if c.direction == "south":
            c.direction = "east"
            return
        if c.direction == "east":
            c.direction = "north"
            return

        #print("left")

    def right(self, space_ahead, c_index):
        c = self.creature_list[c_index]
        if c.direction == "north":
            c.direction = "east"
            return
        if c.direction == "west":
            c.direction = "north"
            return
        if c.direction == "south":
            c.direction = "west"
            return
        if c.direction == "east":
            c.direction = "south"
            return


        #print("right")

    def hop(self, space_ahead, c_index):
        print("hop ", c_index)
        if self.if_empty(space_ahead, c_index) != True:
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
                command(self, space_ahead, c_index)
            j += 1


    def show_board(self):
        for s in self.board:
            print(' '.join(x.symbol for x in s))
        #print(s.split())
        #print(self.board)

    def run(self, n):
        x = 0
        y = 0
        for i in range(n):
            for j in range(len(self.creature_list)):
                c = self.creature_list[j]
                if c.direction == "north":
                    x = c.xcord - 1
                    #print("y: ", y)
                    y = c.ycord
                elif c.direction == "south":
                    x = c.xcord + 1
                    y = c.ycord
                elif c.direction == "west":
                    x = c.xcord
                    y = c.ycord - 1
                elif c.direction == "east":
                    x = c.xcord
                    y = c.ycord + 1

                temp_s = self.board[x][y]
                temp_s.x = x
                temp_s.y = y
                self.play_round(temp_s, j)
                #print("temp_s: ", temp_s)
            print("Round: ", i)
            self.show_board()



            #self.update_creature(j,creature.g)


    def __remove_creature(self, creature, space_ahead):
        self.creature_list.remove(creature)
        self.board[creature.xcord][creature.ycord] = Species(".")
        self.direction_list.remove(creature.direction)


class Species:
    def __init__(self, name):
        """

        :rtype : object
        """
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


# ----
# food
# ----
food = Species("food")
food.add_instruction("left")
food.add_instruction(
    "go 0")  #will have to code for these (split at space, first element is the function to do and the second element is n)

# ------
# hopper
# ------

hopper = Species("hopper")
hopper.add_instruction("hop")
hopper.add_instruction("go 0")

# -----
# rover
# -----

rover = Species("rover")
rover.add_instruction("if_enemy 9")
rover.add_instruction("if_empty 7")
rover.add_instruction("if_random 5")
rover.add_instruction("left")
rover.add_instruction("go 0")
rover.add_instruction("right")
rover.add_instruction("go 0")
rover.add_instruction("hop")
rover.add_instruction("go 0")
rover.add_instruction("infect")
rover.add_instruction("go 0")

# ----
# trap
# ----

trap = Species("trap")
trap.add_instruction("if_enemy 3")
trap.add_instruction("left")
trap.add_instruction("go 0")
trap.add_instruction("infect")
trap.add_instruction("go 0")

print("*** Darwin 7x9 ***")

#seed(0)

Darwin7x9 = Darwin(7, 9)

t1 = Creature(trap)
h1 = Creature(hopper)
r1 = Creature(rover)
t2 = Creature(trap)

Darwin7x9.place_creature(t1, 0, 0, "south")
Darwin7x9.place_creature(h1, 3, 2, "east")
Darwin7x9.place_creature(r1, 5, 4, "north")
Darwin7x9.place_creature(t2, 6, 8, "west")
Darwin7x9.show_board()
Darwin7x9.run(60)

# print("*** Darwin 8x8 ***")

# Darwin8x8 = Darwin(8, 8)
# f1 = Creature(food)
# h1 = Creature(hopper)
# h2 = Creature(hopper)
# h3 = Creature(hopper)
# h4 = Creature(hopper)
# f2 = Creature(food)
# Darwin8x8.place_creature(f1,0,0, "east")
# Darwin8x8.place_creature(h1,3,3, "north")
# Darwin8x8.place_creature(h2,3,4, "east")
# Darwin8x8.place_creature(h3,4,4, "south")
# Darwin8x8.place_creature(h4,4,3, "west")
# Darwin8x8.place_creature(f2,7,7, "north")
# Darwin8x8.show_board()
# Darwin8x8.run(5)

