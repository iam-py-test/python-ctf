"""This is the most basic one (I hope)"""
import random
number = random.choice([0,1,2,3])
inp = input("What's the number? ")
if str(number) == inp:
  print("Hackers always win")
else:
  print("Wrong. The number was {}".format(number))
input()
