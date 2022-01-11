import random
import sys
from myclasses import Person

playerName = input("What is your name? ")
playerAge = int(input("What is your age? "))
player = Person(playerName, playerAge)
deathtally = 3

def main():
  intro(player)

def intro(player):
  print("Welcome to the Federalists,", player.name)
  print("The year is 1801, and Thomas Jefferson was just elected President of America. He is part of the Democratic Republican party, and you are a Federalist, the party that dislikes Jefferson and his message.")
  print("Welcome to 1801, a text-based adventure game with one goal: steal the Declaration of Independence at the National Archives Museum, without being caught by the Democratic Republicans.")
  print("Will you make it out?")
  print("During the game, a command called help will be always available. Good luck!")
  room1(player)
  
def room1(player):
  print(f"In {rooms[0]}: {description[0]}")
  answer = input(" Which door will you pass through, red or yellow? ")
  while not (answer == "red" or answer == "RED" or answer == "yellow" or answer == "YELLOW" or answer == "help"):
    answer = input("Which door will you pass through, red or yellow? ")
  if answer == "red" or answer == "RED":
    red(player)
  if answer == "yellow" or answer == "YELLOW":
    yellow(player)
  elif answer == "help":
    help(player)
    room1(player)

def room2(player):
  print(f"In {rooms[1]}: {description[1]}")
  answer = input("Which door will you open, gold or white? ")
  while not (answer =="gold" or answer == "GOLD" or answer == "white" or answer == "WHITE" or answer == "help"):
    answer = input("Which door will you open, gold or white? ")
  if answer == "gold" or answer == "GOLD":
    gold(player)
  if answer == "white" or answer == "WHITE":
    white(player)
  elif answer == "help":
    help(player)
    room2(player)

def room3(player):
  print(f"In {rooms[2]}: {description[2]}")
  answer = input("Which door will you open, barbed or metal? ")
  while not (answer == "barbed" or answer == "BARBED" or answer == "metal" or answer == "METAL" or answer == "help"):
    answer = input("Which door will you open, barbed or metal? ")
  if answer == "barbed" or answer == "BARBED":
    barbed(player)
  if answer == "metal" or answer == "METAL":
    metal(player)
  elif answer == "help":
    help(player)
    room3(player)
      
def room4(player):
  print(f"In {rooms[3]}: {description[3]}")
  answer = input("You don't have much time, will you go through the light door or thorn door?" )
  while not (answer == "light" or answer == "LIGHT" or answer == "thorn" or answer == "THORN" or answer == "help"):
    answer = input("You don't have much time, will you go through the light door or thorn door? ")
  if answer == "light" or answer == "LIGHT":
    light(player)
  if answer == "thorn" or answer == "THORN":
    thorn(player)
  elif answer == "help":
    help(player)
    room4(player)

def help(player):
  print("Every room only has two options for which door to choose. Each door is given a few words of description: use those wisely.")

def red(player):
  print("Looks like you chose the right door. Good start. Let's keep moving.")
  room2(player)
  
def yellow(player):
  angrypeopleamount = random.randint(3,27)
  print(f"Just kidding. {angrypeopleamount} people see you lurking around without permission so they hit you with batons.")
  for x in range(5):
    player.takeInjury(18)
    print("Someone just hit you!")
    if player.healthlevel == 0:
      death(player)
    else:
      print("You quickly run to the end of the hall and open the nearest door. Somehow, you're in the next room. Lucky chance?")
      room2(player)
  
def barbed(player):
  print("Sheeeeesh! That was a close call. Now, there's only one more choice you have to make. These doors have slogans that are different for each door")
  print("The door on the left has a Martin Van Ruin poster. Seems kinda whiggy...")
  print("The door on the right has a William Harry Harrison poster. Seems kinda sussy..")
  answer = input("Will you whiggy through the the Van Ruin door or the Whiggy door? ")
  while not (answer == "van Ruin" or answer == "VAN RUIN" or answer == "whiggy" or answer == "WHIGGY" or answer == "help"):
    answer = input("Time is running out, will you whiggy through the the Van Ruin door or the Whiggy door? ")
  if answer == "whiggy" or answer == "WHIGGY":
    room4(player)
  if answer == "van ruin" or answer == "VAN RUIN":
    death(player)
  elif answer == "help":
    help(player)
    room1(player)
      
def metal(player):
  print("Unfortunately, the metal door leads to the Lapis Library where John Adams captures and takes back the Declaration of Independence")
  death(player)

def light(player):
  print("You reach for the knob of the light door and see a shadow approaching instead. You halt to see Alexander Hamilton facing you from the other side of the door with open arms.")
  print("You realize that your hair has gone grey and your hands are covered in wrinkles... did it really take that long?")
  player.increaseAge(10)
  print("He smiles when he sees the Declaration of Independence in your hand and you did it. Congrats!")
  finale(player)

def thorn(player):
  print("You carefully creep through the door, watching the thorns near your clothes to make sure you don't-")
  player.takeInjury(40)
  print("The thorns pierce into your skin, and you start to struggle making it out.")
  player.takeInjury(20)
  print("Another thorn cuts you, oh jeez. Hurry up!")
  player.takeInjury(30)
  print("You are at the brink of death, it would be a miracle if you made it out.")
  print(".....")
  if player.healthLevel == 0:
    death(player)
  else:
    print("Somehow you made it out. I am genuinely surprised.")
    finale(player)

def finale(player):
  print(f"Congratulations on making it out! The Federalist party is more powerful than ever, all thanks to you, {playerName}.")
  print("SUMMARY")
  print(f"Health: {player.healthLevel}")
  print(f"Age: {player.Age}")
  print(f"Death Tally: {deathtally}")

def gameover(player):
  print("Your choices led to your downfall, GAME OVER.")
  print("SUMMARY")
  print(f"Health: {player.healthLevel}")
  print(f"Age: {player.Age}")
  print(f"Death Tally: {deathtally}")
  restart = input("Play again? ")
  if restart == "Yes" or restart == "yes":
    main()
  else:
    print("Thank you for playing.")
    sys.exit

def death(player):
  deathtally == deathtally - 1
  if deathtally == 0:
    gameover(player)
  else:
    print(f"You have lost all your health due to your choice! You will start back at the beginning. You have {deathtally} lives left. ")
    player.healFull
    room1(player)

def gold(player):
  print("You slowly turn the door handle to find a empty hallway, but you hear faint footsteps.")
  print("Did you just save yourself for something? Nevermind. There is a sign on the wall that says Way to Archives with an arrow. Better keep moving.")
  room3(player)

def white(player):
  print("You open the door to find James Madison, Jefferson's most trusted friend, writing a bill on his desk. Is that the Bill of Rights?")
  print("He looks up and meets you gaze, and then grabs his dagger to fight.")
  player.takeInjury(20)
  print("His dagger scratches your arm and you lose 20 health!")
  print("Better make a run for it!")
  print(".....")
  print("James Madison caught you. Good try rookie.")
  death(player)

rooms = ["Room 1" , "Room 2" , "Room 3", "Room 4"]
description = ["You enter into the National Archives Museum, and there are two doors. One door is red that you hear voices from, and one door is yellow which leads into a unknown hallway" , "You enter into the main hallway, with one door on either side of the hall. One door is engraved with latin sayings in gold, and the other is a white door with the label J.M.] on it." , "You enter into the Hallowed Hallway, with the Lapis Library through the barbed door and the Happy Hallway behind the metal door." , "You are almost out of the National Archives Museum, but there is one room left. There are two small doors, you'll have to bend down to fit through. The door on the left is a open pane window, showing light but not a outside world. A little strange. The door on the right has a doorframe made of thorns, it would take longer to get through."]

main()
