import random
n=random.randint(1,100)
while True:
  x=int(input("enter the value of x"))
  print("Guess the number")
  if(x<n):
    print("too low")
  elif(x>n):
    print("too high")
  else:
    print("GAME OVER")
