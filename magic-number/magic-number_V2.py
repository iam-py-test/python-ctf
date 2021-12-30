import random
playing = True
points = 0

chelp = """
[number]: Check if that number is the answer
math: Evaluate an math expression (i.e. 1+1)
points: Display the current points
reset: Reset the game
end: End the game
help: Display this help message
"""

badmaths = ["randnumb","rdnumb","print(randnumb)","print(rdnumb)","print(\"Hacked\" + rdnumb)"]

while playing:
  rdnumb = random.randrange(0,10000)
  got = False
  while got == False:
    cmd = input("What is the magic number? ")
    if cmd == str(rdnumb):
      print("Got it! ")
      got = True
      points += 1
    elif cmd.startswith("math "):
      ma = cmd.replace("math ","")
      if ma in badmaths:
        ma = ""
      try:
        evaled = eval(ma)
        print("{}".format(evaled))
      except:
        print("Math crashed")
        continue
    elif cmd == "points":
      print("Points: {}".format(points))
    elif cmd == 'reset':
      got = True
      points = 0
    elif cmd == "end":
      got = None
      playing = False
    elif cmd == "help":
      print(chelp)
    else:
      try:
        int(cmd)
      except:
        print("Command {} not found".format(cmd))
        print(chelp)
      else:
        print("Wrong number")

print("---- Game over ----")
print("Points: {}".format(points))
