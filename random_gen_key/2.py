import random
number = random.randrange(1,10000)
ni = input("What's the secret number? ")
try:
  if int(ni) == number:
    print("Hackers are the best")
  else:
    print("Incorrect")
except:
  print("Wrong type")
