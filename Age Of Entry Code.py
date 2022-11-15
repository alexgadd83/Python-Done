"""write a code for a way of detecting the age
of somebody"""

Age = input("What is your age?")
if (int(Age)) >= 18:
  print(str("Welcome In"))
else:
  if (int(Age)) < 18:
    print(str("You are too young to enter"))