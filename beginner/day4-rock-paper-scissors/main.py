rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

options = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")

player = int(input())

if player < 0 or player > 2:
  print("You typed an invalid input, you lose!")
else: 
  print(options[player])

  computer = random.randint(0, 2)

  print("Computer chose: ")

  print(options[computer])
  
  if player == 0 and computer == 2:
    print("You win!")
  if computer == 2 and player == 0:
    print("You lose!")
  elif player > computer:
      print("You win!")
  elif player == computer:
      print("It's a draw!")
  else:
      print("You lose!")
  
