# TestDarwin.py
#ibrahim_nagib_IN2422

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Darwin1 import Darwin, Creature, Species

# -----------
# Test Darwin
# -----------

class TestDarwin (TestCase):

    # -------
    # Species
    # -------

    def test_Species_1(self):
        assert hasattr(Species, "add_instruction")

    def test_Species_2(self):
        food = Species("food")
        self.assertEqual(food.name, "food")
        self.assertEqual(food.symbol, "f")


    def test_Species_3(self):
        s = Species("rover")
        s.add_instruction("hop")
        self.assertEqual(s.instruction_list[0], "hop")

    def test_Species_4(self):
        s = Species("s")
        self.assertEqual(s.instruction_list, [])

    def test_Species_5(self):
        s = Species("food")
        s.add_instruction("hop")
        self.assertEqual(len(s.instruction_list), 1)

    def test_Species_6(self):
        s = Species("food")
        s.add_instruction("infect")
        s.add_instruction("hop")
        self.assertEqual(len(s.instruction_list), 2)

    def test_Species_7(self):
        s = Species("food")
        s.add_instruction("hop")
        self.assertEqual(s.instruction_list, ["hop"])

    def test_Species_8(self):
        s = Species("food")
        s.add_instruction("infect")
        s.add_instruction("hop")
        self.assertEqual(s.instruction_list, ["infect", "hop"])


    # --------
    # Darwin
    # --------

    def test_Darwin_1(self):
        assert hasattr(Darwin, "go")
        game = Darwin(5,5)
        self.assertEqual(game.x_axis,5)
        self.assertEqual(game.y_axis,5)

    def test_Darwin_2(self):
        assert hasattr(Darwin, "if_random")
        game = Darwin(2,2)
        self.assertEqual(game.creature_list,[])

    def test_Darwin_3(self):
        assert hasattr(Darwin, "left")
        game = Darwin(4,4)
        self.assertEqual(game.species_list,[])

    def test_Darwin_4(self):
        assert hasattr(Darwin, "right")
        game = Darwin(5,5)
        food = Species("food")
        c = Creature(food)
        game.place_creature(c,2,2,"east")
        self.assertEqual(c.direction,"east")
        game.left(0,0)
        self.assertEqual(c.direction,"north")
        game.left(0,0)
        self.assertEqual(c.direction,"west")
        game.left(0,0)
        self.assertEqual(c.direction,"south")
        game.left(0,0)
        self.assertEqual(c.direction,"east")

  
    def test_Darwin_5(self):
        assert hasattr(Darwin, "hop")
        game = Darwin(6,6)
        rover = Species("rover")
        c = Creature(rover)
        game.place_creature(c,2,3,"east")
        self.assertEqual(c.direction,"east")
        game.right(0,0)
        self.assertEqual(c.direction,"south")

	def test_Darwin_6(self):
		assert hasattr(Darwin, "place_creature")
        game = Darwin(5,5)
        food = Species("food")
        b = Creature(food)
        game.place_creature(b,2,2,"west")
        self.assertEqual(b.direction,"west")
        game.left(0,0)
        self.assertEqual(b.direction,"south")

    def test_Darwin_7(self):
        assert hasattr(Darwin, "show_board")
        game = Darwin(5,5)
        trap = Species("trap")
        c = Creature(trap)
        game.place_creature(c,2,2,"north")
        self.assertEqual(c.direction,"north")
        game.left(0,0)
        self.assertEqual(c.direction,"west")

    def test_Darwin_8(self):
        assert hasattr(Darwin, "if_empty")
        game = Darwin(7,7)
        food = Species("food")
        c = Creature(food)
        game.place_creature(c,4,4,"north")
        self.assertEqual(c.direction,"north")
        game.right(0,0)
        self.assertEqual(c.direction,"east")
        game.right(0,0)
        self.assertEqual(c.direction,"south")
        game.right(0,0)
        self.assertEqual(c.direction,"west")

    def test_Darwin_9(self):
        assert hasattr(Darwin, "if_wall")
        game = Darwin(5,5)
        food = Species("food")
        c = Creature(food)
        space = Species(".")
        game.place_creature(c,2,2,"east")
        self.assertEqual(c.direction,"east") 
        b = game.if_empty(space,0)
        self.assertEqual(b,True)       

    def test_Darwin_10(self):
        assert hasattr(Darwin, "if_enemy")
        game = Darwin(5,5)
        food = Species("food")
        c = Creature(food)
        space = Species(".")
        game.place_creature(c,2,2,"east")
        self.assertEqual(c.direction,"east") 
        b = game.if_empty(food,0) 
        self.assertEqual(b,False)

    def test_Darwin_11(self):
        assert hasattr(Darwin, "infect")
        game = Darwin(5,5)
        rover = Species("rover")
        c = Creature(rover)
        space = Species(".")
        game.place_creature(c,2,2,"west")
        self.assertEqual(c.direction,"west") 
        v = game.if_enemy(space,False) 

    def test_Darwin_12(self):
        assert hasattr(Darwin, "play_round")
        game = Darwin(5,5)
        food = Species("food")
        c = Creature(food)
        space = Species(".")
        game.place_creature(c,2,2,"south")
        self.assertEqual(c.direction,"south") 
        v = game.if_enemy(c,0) 
        self.assertEqual(v, True)

    def test_Darwin_13(self):
        assert hasattr(Darwin, "run")



    # -------
    # Creature
    # -------


    def test_Creature_1(self):
        food = Species("food")
        f = Creature(food)
        self.assertEqual(f.species.name, "food")

    def test_Creature_2(self):
        rover = Species("rover")
        r = Creature(rover)
        self.assertEqual(r.species.name, "rover")
        self.assertEqual(r.species.symbol, "r")

    def test_Creature_3(self):
        food = Species("food")
        f = Creature(food)
        self.assertEqual(f.species.name, "food")

    def test_Creature_4(self):
        rover = Species("rover")
        r = Creature(rover)
        self.assertEqual(r.species.name, "rover")
        self.assertEqual(r.species.symbol, "r")

    def test_Creature_5(self):
        food = Species("food")
        f = Creature(food)
        self.assertEqual(f.species.name, "food")

    def test_Creature_6(self):
        rover = Species("rover")
        r = Creature(rover)
        self.assertEqual(r.species.name, "rover")
        self.assertEqual(r.species.symbol, "r")

    def test_Creature_7(self):
        food = Species("food")
        f = Creature(food)
        self.assertEqual(f.species.name, "food")

    def test_Creature_8(self):
        rover = Species("rover")
        r = Creature(rover)
        self.assertEqual(r.species.name, "rover")
        self.assertEqual(r.species.symbol, "r")
    

main()
