import random
import os
playing = True
points = 0
while playing:
  randnumb = random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55])
  gotit = False
  while gotit == False:
    cmd = input("What's the magic number? ")
    if cmd == str(randnumb):
      print("Got it! ")
      gotit = True
      points += 1
    elif cmd.startswith("math: "):
      ma = cmd.split("math: ")[0]
      print(ma)
      evaled = eval(ma)
      print("{}".format(evaled))
    elif cmd == "getpoints":
      print("Points: {}".format(points))
    elif cmd == "end":
      gotit = None
      playing = False

print("---- Game over ----")
print("Points: {}".format(points))
