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
from Darwin1 import *

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

Darwin8x8.run(5)

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

Darwin7x9.place_creature(t1, 0, 0, "South")
Darwin7x9.place_creature(h1, 3, 2, "East")
Darwin7x9.place_creature(r1, 5, 4, "North")
Darwin7x9.place_creature(t2, 6, 8, "West")

Darwin7x9.run(5)

# ------------
# darwin 72x72
# without best
# ------------

print("*** Darwin 72x72 without Best ***")
seed(0)

Darwin72_wob = Darwin(72, 72)
# 10 food
y, x, d = random_placer(72, 72)
f1 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f2 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f3 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f4 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f5 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f6 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f7 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f8 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f9 = Creature(food, y, x, d)
y, x, d = random_placer(72, 72)
f10 = Creature(food, y, x, d)

# 10 hopper
y, x, d = random_placer(72, 72)
h1 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h2 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h3 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h4 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h5 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h6 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h7 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h8 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h9 = Creature(hopper, y, x, d)
y, x, d = random_placer(72, 72)
h10 = Creature(hopper, y, x, d)

#10 rover
y, x, d = random_placer(72, 72)
r1 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r2 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r3 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r4 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r5 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r6 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r7 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r8 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r9 = Creature(rover, y, x, d)
y, x, d = random_placer(72, 72)
r10 = Creature(rover, y, x, d)

# 10 trap
y, x, d = random_placer(72, 72)
t1 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t2 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t3 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t4 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t5 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t6 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t7 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t8 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t9 = Creature(trap, y, x, d)
y, x, d = random_placer(72, 72)
t10 = Creature(trap, y, x, d)


Darwin72_wob.place_creature(f1)
Darwin72_wob.place_creature(f2)
Darwin72_wob.place_creature(f3)
Darwin72_wob.place_creature(f4)
Darwin72_wob.place_creature(f5)
Darwin72_wob.place_creature(f6)
Darwin72_wob.place_creature(f7)
Darwin72_wob.place_creature(f8)
Darwin72_wob.place_creature(f9)
Darwin72_wob.place_creature(f10)

Darwin72_wob.place_creature(h1)
Darwin72_wob.place_creature(h2)
Darwin72_wob.place_creature(h3)
Darwin72_wob.place_creature(h4)
Darwin72_wob.place_creature(h5)
Darwin72_wob.place_creature(h6)
Darwin72_wob.place_creature(h7)
Darwin72_wob.place_creature(h8)
Darwin72_wob.place_creature(h9)
Darwin72_wob.place_creature(h10)

Darwin72_wob.place_creature(r1)
Darwin72_wob.place_creature(r2)
Darwin72_wob.place_creature(r3)
Darwin72_wob.place_creature(r4)
Darwin72_wob.place_creature(r5)
Darwin72_wob.place_creature(r6)
Darwin72_wob.place_creature(r7)
Darwin72_wob.place_creature(r8)
Darwin72_wob.place_creature(r9)
Darwin72_wob.place_creature(r10)

Darwin72_wob.place_creature(t1)
Darwin72_wob.place_creature(t2)
Darwin72_wob.place_creature(t3)
Darwin72_wob.place_creature(t4)
Darwin72_wob.place_creature(t5)
Darwin72_wob.place_creature(t6)
Darwin72_wob.place_creature(t7)
Darwin72_wob.place_creature(t8)
Darwin72_wob.place_creature(t9)
Darwin72_wob.place_creature(t10)


Darwin72_wob.run(1000)

