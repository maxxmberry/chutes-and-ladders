import random
gameBoard=[ ]
for i in range(101):
  gameBoard.append(len(gameBoard))

print('Welcome to Chutes and Ladders. Your objective in this game is to be the first person to reach the top of the board. You will roll a die to advance your pawn up the board. Here are the rules: \n1. If your turn ends on the bottom of a ladder, the program will send you up closer to the end \n2. If your turn ends on the top of a chute, the program will send you right back down the board to where the chute ends \n3. To reach the 100th spot, you need to roll the perfect number of spaces in order to land on it. If you roll a number higher than you need, you will not advance at all on that turn \n4.---- \n')

ladders=[1, 4, 9, 21, 28, 36, 51, 71, 90]
topladders=[38, 42, 9, 21, 28, 36, 51, 71, 90]
chutes=[16, 47, 49, 56, 62, 64, 87, 93, 95, 98]
playerOneName=input('What is your name, player one? ')
playerOneSpace=0
playerOneMove=0
playerTwoName=input('What is your name, player two? ')
playerTwoSpace=0
playerTwoMove=0

newLadderSpot=0
newChuteSpot=0
ladderFlag=False
chuteFlag=False

# can have multiple players
# numPlayers=int(input('How many people are playing? (2 max) '))

# player location on board will be shown through list

def dice_roller(player_space, player_name):
  diceRoll=random.randint(1,6)
  print(player_name, 'rolled a', diceRoll)
  if player_space + diceRoll > 100:
    print('You rolled over 100, try again')
    player_space = player_space
  else: 
    player_space+=diceRoll
  return player_space

def ladder_scenario(player_space, high_number):
  print('You landed on a ladder!')
  player_space=high_number
  return player_space

def chute_scenario(player_space, low_number):
  print('You landed on a chute.. Down you go.')
  player_space=low_number
  return player_space

def ladder_checker(player_space):
  global newLadderSpot
  if player_space==1:
    newLadderSpot=ladder_scenario(player_space, 38)
    # print(newLadderSpot)
    # print('before:', player_space)
    player_space=newLadderSpot
    # print('after:', player_space)
  elif player_space==4:
    newLadderSpot=ladder_scenario(player_space, 14)
    # print(newLadderSpot)
    # print('before:', player_space)
    player_space=newLadderSpot
    # print('after:', player_space)
  elif player_space==9:
    newLadderSpot=ladder_scenario(player_space, 38)
    # print(newLadderSpot)
    # print('before:', player_space)
    player_space=newLadderSpot
    # print('after:', player_space)
  elif player_space==21:
    newLadderSpot=ladder_scenario(player_space, 42)
    player_space=newLadderSpot
  elif player_space==28:
    newLadderSpot=ladder_scenario(player_space, 84)
    player_space=newLadderSpot
  elif player_space==36:
    newLadderSpot=ladder_scenario(player_space, 44)
    player_space=newLadderSpot
  elif player_space==51:
    newLadderSpot=ladder_scenario(player_space, 67)
    player_space=newLadderSpot
  elif player_space==71:
    newLadderSpot=ladder_scenario(player_space, 91)
    player_space=newLadderSpot
  elif player_space==90:
    newLadderSpot=ladder_scenario(player_space, 100)
    player_space=newLadderSpot
  return newLadderSpot

def chute_checker(player_space):
  global newChuteSpot
  if player_space==16:
    newChuteSpot=chute_scenario(player_space, 38)
    player_space=newChuteSpot
  elif player_space==47:
    newChuteSpot=chute_scenario(player_space, 26)
    player_space=newChuteSpot
  elif player_space==49:
    newChuteSpot=chute_scenario(player_space, 11)
    player_space=newChuteSpot
  elif player_space==56:
    newChuteSpot=chute_scenario(player_space, 53)
    player_space=newChuteSpot
  elif player_space==62:
    newChuteSpot=chute_scenario(player_space, 19)
    player_space=newChuteSpot
  elif player_space==64:
    newChuteSpot=chute_scenario(player_space, 60)
    player_space=newChuteSpot
  elif player_space==87:
    newChuteSpot=chute_scenario(player_space, 24)
    player_space=newChuteSpot
  elif player_space==93:
    newChuteSpot=chute_scenario(player_space, 73)
    player_space=newChuteSpot
  elif player_space==95:
    newChuteSpot=chute_scenario(player_space, 75)
    player_space=newChuteSpot
  elif player_space==98:
    newChuteSpot=chute_scenario(player_space, 78)
    player_space=newChuteSpot
  return newChuteSpot

def special_spaces_checker(player):
  ladder_checker(player)
  chute_checker(player)

while playerOneMove !=100 and playerTwoMove != 100:
  pause=input('\nClick \'ENTER\' when you are ready for the next turn ')

  playerOneMove=dice_roller(playerOneSpace, playerOneName)
  playerOneSpace= playerOneMove
  p1Checker=special_spaces_checker(playerOneSpace)
  print('p1Checker:', p1Checker)
  print('')

  playerTwoMove=dice_roller(playerTwoSpace, playerTwoName)
  playerTwoSpace= playerTwoMove
  p2Checker=special_spaces_checker(playerTwoSpace)

  # playerOneSpace=p1Checker
  # playerTwoSpace=p2Checker
  print('')
  print(playerOneName, playerOneSpace)
  print(playerTwoName, playerTwoSpace)

  #NEXT PROBLEM: ladder/chute move adds to player's spot, but once they land on one, their position is stuck