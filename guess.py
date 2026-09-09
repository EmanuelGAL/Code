def tutorial(n):
    enter = input("The game is simple. Theres a Murderer, The Room the murder happened, And the weapon used (Press ENTER To Continue) ")
    enter = input("Each Player has a turn to guess each of the things above (Press ENTER To Continue) ")
    enter = input("The game ends when each aspect has been guessed correctly, Good Luck! (Press ENTER To Start Game) ")
    MurderGame(n)

def MurderGame(n):
  Players = [" "]*n
  for i in range(n):
      Players[i] = input("What will Player " + str(i+1) + "'s name be? ")
  enter = input("Here are the Players: "+ str(Players))
  
  import random
  
  names = ["PROFESSOR PLUM", "MRS WHITE", "MR GREEN", "MRS PEACOCK", "MISS SCARLET", "COLONEL MUSTUARD"]
  rooms = ["STUDY", "KITCHEN", "HALL", "CONSERVATORY", "LOUNGE", "BALLROOM", "DINING ROOM", "LIBRARY", "BILLIARD ROOM"]
  weapons = ["WRENCH", "CANDLESTICK", "LEAD PIPE", "PIPE", "REVOLVER", "KNIFE"]

  Mnum = random.randint(0,5)
  Rnum = random.randint(0,9)
  Wnum = random.randint(0,5)

  Murderer = names[Mnum]
  Room = rooms[Rnum]
  Weapon = weapons[Wnum]

  tries = 10
  correct = 0
  status = "false"
  
  print("")

  while status == "false":
    CurPlayer = 0
    enter = input("It is now " + Players[CurPlayer] + "'s turn (Press ENTER To Continue) ")
    
    print("Who do you think the murderer is? Options are:", names)
    Mguess = input()
    Mguess = Mguess.upper()

    print("What room do you think the murder happened? Options are:", rooms)
    Rguess = input()
    Rguess = Rguess.upper()

    print("What weapons do you think was used?? Options are:", weapons)
    Wguess = input()
    Wguess = Wguess.upper()

    if Mguess == Murderer:
      correct += 1
    else:
      correct += 0

    if Rguess == Room:
      correct += 1
    else:
      correct += 0

    if Wguess == Weapon:
      correct += 1
    else:
      correct += 0

    tries -= 1
    
    if tries == 0:
        print("You failed...")
        print("The Murderer was:", Murderer)
        print("The Room was:", Room)
        print("The Weapon was:", Weapon)
        status = "true"
    else:
        if correct == 3:
          print("You Guessed All Correctly!")
          status = "true"
        else:
          yesNo = input("You got "+ str(correct) + "/3 , Would You Like To Play Again? (yes/no)")
          yesNo = yesNo.lower()
          if yesNo == "no":
            status = "true"
          else:
            status = "false"

NumPlayers = int(input("Welcome to the Murderer Game, How many players are there? : "))
random = input("Would you like a tutorial? (yes/no) : ")
random = random.lower()
if random == "yes":
    tutorial(NumPlayers)
else:
    enter = input("Press ENTER To Start Game")
    MurderGame(NumPlayers)

  
