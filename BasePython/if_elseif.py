print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM? \n= "))

if height >= 120:
  print("Yes you can ride the rollercoaster!")
  age = int(input("What is your age? \n= "))
  if(age <= 18):
    print("Ticket price is $7")
  else:
    print("Ticket price is $12")
else:
  print("Sorry, you can't play this one")