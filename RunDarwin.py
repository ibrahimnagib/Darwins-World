# Ibrahim Nagib
# In 2422
# -----------------------------
# projects/collatz/RunDarwin.py
# Copyright (C) 2014
# Glenn P. Downing
# -----------------------------

# -------
# imports
# -------

from random import seed
import sys
from Darwin3 import *

# ----
# food
# ----

food = Species("food")
food.add_instruction("left")
food.add_instruction("go 0")


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
trap.add_instruction("left")
trap.add_instruction("go 0")
trap.add_instruction("infect")
trap.add_instruction("go 0")


# ----
# best
# ----




best = Species("best")
best.add_instruction("if_enemy 10")
best.add_instruction("if_empty 7")
best.add_instruction("if_random 5")
best.add_instruction("left")
best.add_instruction("go 0")
best.add_instruction("right")
best.add_instruction("go 0")
best.add_instruction("hop")
best.add_instruction("if_enemy 10")
best.add_instruction("go 0")
best.add_instruction("infect")
best.add_instruction("go 0")

# ----------
# Randomizer
# ----------

def randomizer(l,w):
	x = random.randrange(0,l)
	y = random.randrange(0,w)
	d = random.randrange(0,4)
	direction_list = ["west","north","east","south"]
	direction = direction_list[d]
	return x,y,direction




# ----------
# darwin 8x8
# ----------

print("*** Darwin 8x8 ***")

Darwin8x8 = Darwin(8, 8)
f1 = Creature(food)
h1 = Creature(hopper)
h2 = Creature(hopper)
h3 = Creature(hopper)
h4 = Creature(hopper)
f2 = Creature(food)
Darwin8x8.place_creature(f1,0,0, "east")
Darwin8x8.place_creature(h1,3,3, "north")
Darwin8x8.place_creature(h2,3,4, "east")
Darwin8x8.place_creature(h3,4,4, "south")
Darwin8x8.place_creature(h4,4,3, "west")
Darwin8x8.place_creature(f2,7,7, "north")

Darwin8x8.run(6)

# ----------
# darwin 7x9
# ----------

print("*** Darwin 7x9 ***")

seed(0)

Darwin7x9 = Darwin(7, 9)

t1 = Creature(trap)
h1 = Creature(hopper)
r1 = Creature(rover)
t2 = Creature(trap)

Darwin7x9.place_creature(t1, 0, 0, "south")
Darwin7x9.place_creature(h1, 3, 2, "east")
Darwin7x9.place_creature(r1, 5, 4, "north")
Darwin7x9.place_creature(t2, 6, 8, "west")

Darwin7x9.run(6)

# ------------
# darwin 72x72
# without best
# ------------

print("*** Darwin 72x72 without Best ***")
seed(0)

Darwin72_wob = Darwin(72, 72)
# 10 food


f1 = Creature(food)
f2 = Creature(food)
f3 = Creature(food)
f4 = Creature(food)
f5 = Creature(food)
f6 = Creature(food)
f7 = Creature(food)
f8 = Creature(food)
f9 = Creature(food)
f10 = Creature(food)


x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f10,x,y,d)


# 10 hopper

h1 = Creature(hopper)
h2 = Creature(hopper)
h3 = Creature(hopper)
h4 = Creature(hopper)
h5 = Creature(hopper)
h6 = Creature(hopper)
h7 = Creature(hopper)
h8 = Creature(hopper)
h9 = Creature(hopper)
h10 = Creature(hopper)

x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(h10,x,y,d)

#10 rover

r1 = Creature(rover)
r2 = Creature(rover)
r3 = Creature(rover)
r4 = Creature(rover)
r5 = Creature(rover)
r6 = Creature(rover)
r7 = Creature(rover)
r8 = Creature(rover)
r9 = Creature(rover)
r10 = Creature(rover)

x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(r10,x,y,d)

# 10 trap

t1 = Creature(trap)
t2 = Creature(trap)
t3 = Creature(trap)
t4 = Creature(trap)
t5 = Creature(trap)
t6 = Creature(trap)
t7 = Creature(trap)
t8 = Creature(trap)
t9 = Creature(trap)
t10 = Creature(trap)


x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(t10,x,y,d)


Darwin72_wob.run(1001)


# ------------
# darwin 72x72
# with best
# ------------

print("*** Darwin 72x72 with Best ***")
seed(0)

Darwin72_wb = Darwin(72, 72)


# 10 food


f1 = Creature(food)
f2 = Creature(food)
f3 = Creature(food)
f4 = Creature(food)
f5 = Creature(food)
f6 = Creature(food)
f7 = Creature(food)
f8 = Creature(food)
f9 = Creature(food)
f10 = Creature(food)


x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wob.place_creature(f3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(f10,x,y,d)


# 10 hopper

h1 = Creature(hopper)
h2 = Creature(hopper)
h3 = Creature(hopper)
h4 = Creature(hopper)
h5 = Creature(hopper)
h6 = Creature(hopper)
h7 = Creature(hopper)
h8 = Creature(hopper)
h9 = Creature(hopper)
h10 = Creature(hopper)

x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(h10,x,y,d)

#10 rover

r1 = Creature(rover)
r2 = Creature(rover)
r3 = Creature(rover)
r4 = Creature(rover)
r5 = Creature(rover)
r6 = Creature(rover)
r7 = Creature(rover)
r8 = Creature(rover)
r9 = Creature(rover)
r10 = Creature(rover)

x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(r10,x,y,d)

# 10 trap

t1 = Creature(trap)
t2 = Creature(trap)
t3 = Creature(trap)
t4 = Creature(trap)
t5 = Creature(trap)
t6 = Creature(trap)
t7 = Creature(trap)
t8 = Creature(trap)
t9 = Creature(trap)
t10 = Creature(trap)


x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(t10,x,y,d)

# 10 best

b1 = Creature(best)
b2 = Creature(best)
b3 = Creature(best)
b4 = Creature(best)
b5 = Creature(best)
b6 = Creature(best)
b7 = Creature(best)
b8 = Creature(best)
b9 = Creature(best)
b10 = Creature(best)


x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b1,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b2,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b3,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b4,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b5,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b6,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b7,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b8,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b9,x,y,d)
x, y, d = randomizer(72, 72)
Darwin72_wb.place_creature(b10,x,y,d)


Darwin72_wb.run(1001)
