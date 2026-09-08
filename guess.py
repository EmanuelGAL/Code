def MurderGame():
  import random
  names = ["PROFESSOR PLUM", "MRS WHITE", "MR GREEN", "MRS PEACOCK", "MISS SCARLET", "COLONEL MUSTUARD"]
  rooms = ["STUDY", "KITCHEN", "HALL", "CONSERVATORY", "LOUNGE", "BALLROOM", "DINING ROOM", "LIBRARY", "BILLIARD ROOM"]
  weapons = ["WRENCH", "CANDLESTICK", "LEAD PIPE", "PIPE", "REVOLVER", "KNIFE"]

  Mnum = random.randint(0,5)
  Rnum = random.randint(0,9)
  Wnum = random.randint(0,5)

  Murderer = names[Munm]
  Room = rooms[Rnum]
  Weapon = weapons[Wnum]

  tries = 10
  correct = 0
  status = "false"

  while status == "false":
    print("Who do you think the murderer is? Options are:", names)
    Mguess = input()
    Mguess.lower()

    print("What room do you think the murder happened? Options are:", rooms)
    Rguess = input()
    Rguess.lower()

    print("What weapons do you think was used?? Options are:", weapons)
    Wguess = input()
    Wguess.lower()

    if Mguess == Murderer:
      correct += 1
    else:
      correct += 0

    if Rguess == Room:
      correct += 1
    else:
      correct += 0

    if Wguess == Weapons:
      correct += 1
    else:
      correct += 0

    tries -= 1

    if correct == 3:
      print("You Guessed All Correctly!")
      status = "true"
    else:
      print("You got", correct + "/3 , You have", tries, "tries remanining")
      status = "false"

MurderGame()
      
  
