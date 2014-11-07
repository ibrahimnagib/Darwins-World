# Darwin.py
# Ibrahim Nagib
# In 2422
import random


class Darwin:
    """
    Class Darwin creates a board, creates lists for species, and creatures,
    Darwin is responsible for adding creatures to the game, updating creatures, 
    and moving the creatures on the board, only darwin knows what is on the board, 
    and what is in front of each creature. 

    """
    def __init__(self, x_axis, y_axis):
        self.x_axis = int(x_axis)
        self.y_axis = int(y_axis)
        self.species_list = []
        self.direction_list = []
        self.creature_list = []

        """
        empty space and wall are both made by creating a species 
        instances of each so that the rest of the creatures can easily
        and homogeneously communinicate with them through darwin

        """

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
        """
        places a new creature on the board,
        also called when a creature is infected, 
        ro re-initiate an instance of the infector
        """
        self.board[(start_x + 1)][start_y + 1] = creature.species
        creature.direction = direction
        creature.xcord = start_x + 1
        creature.ycord = start_y + 1

        self.creature_list.append(creature)
        self.direction_list.append(direction)

        """
        Darwin has all of the controls and actions
        so that only the game instance (Darwin class object)
        has access to the board and al moves
        """

    def if_empty(self, space_ahead, c_index):
        empty = Species(".")
        if space_ahead.name == empty.name:
            return True
        else:
            return False


    def if_random(self, space_ahead, c_index):
        if random.randrange(0, 2) % 2 == 0:
            return True
        else:
            return False

    def go(self, space_ahead, c_index):
        return True


    def if_enemy(self, space_ahead, c_index):
        empty = Species(".")
        wall = Species("*")
        s = self.creature_list[c_index].species

        if space_ahead.name == empty.name:
            return False

        elif space_ahead.name == wall.name:
            return False

        elif space_ahead.name == s.name:
            return False

        else:
            return True


    """
    actions
    """
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

    def hop(self, space_ahead, c_index):
        if self.if_empty(space_ahead, c_index) != True:
            return
        else:
            empty = Species(".")
            c = self.creature_list[c_index]
            self.board[c.xcord][c.ycord] = empty

        if c.direction == "north":
            c.xcord -= 1
        if c.direction == "south":
            c.xcord += 1
        if c.direction == "west":
            c.ycord -= 1
        if c.direction == "east":
            c.ycord += 1
        self.board[c.xcord][c.ycord] = c.species

    def play_round(self, space_ahead, c_index):
        """
        used a for-loop for the play round function but 
        added an integer j, that is used to determine the 
        creature number that is playing the turn in the round,
        the round terminates when i==j.
        """
        j = 0
        s = self.creature_list[c_index].species
        for i in range(len(s.instruction_list)):
            if i != j:
                continue
            r = s.instruction_list[i]
            if " " in r:
                r = r.split(" ")
                command = getattr(Darwin, r[0])
                if command(self, space_ahead, c_index) == True:
                    j = int(r[1])
                    if j == 0:
                        break
                    continue
            else:
                command = getattr(Darwin, r)
                command(self, space_ahead, c_index)
            j += 1


    def show_board(self):
        """
        shows board by printing each array in the 2d array
        on a new line, seperated by spaces
        """
        for s in self.board:
            print(' '.join(x.symbol for x in s))

    def run(self, n):
        x = 0
        y = 0
        for i in range(n):
            for j in range(len(self.creature_list)):
                c = self.creature_list[j]
                if c.direction == "north":
                    x = c.xcord - 1
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

            if self.x_axis<20:
                print("Round: ", i)
                self.show_board()
            else:
                if i<10:
                    print("Round: ", i)
                    self.show_board()
                else:
                    if i%100==0:
                        print("Round: ", i)
                        self.show_board()

    def __remove_creature(self, creature, space_ahead):
        """
        used for removing a creatures instance, and removing
        that creature from the creature_list if it becomes 
        infected
        """
        self.creature_list.remove(creature)
        self.board[creature.xcord][creature.ycord] = Species(".")
        self.direction_list.remove(creature.direction)


class Species:
    """
    class Species initiates a type species, each species has a unique
    set of instructions, stored in the instruction_list in the Species
    class, it also has a name, and a symbol which is simple name[0]
    """
    def __init__(self, name):

        self.name = name
        self.symbol = name[0]
        self.instruction_list = []
        self.x = 0
        self.y = 0

    def __str__(self):
        return self.name

    def add_instruction(self, instruction):
        """
        adds instructions to the instruction_list
        """
        self.instruction_list.append(instruction)


class Creature:
    """
    class Creature is responsible for initiating
    different instances of creatures that are of a certain species,
    it takes as an argument, only the type of species, the starting 
    coordinates of the creature are given to Darwin class when placing the creatures 
    on the board.
    """
    def __init__(self, species):
        self.species = species
        self.direction = ''
        self.xcord = 0
        self.ycord = 0
        self.counter = 0

    def __str__(self):
        return self.species
