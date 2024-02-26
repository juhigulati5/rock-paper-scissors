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

import random

rps_list = [rock, paper, scissors]

rps = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))

if rps < 0 or rps>= 3:
  print("You typed an invalid number, you lose!")
else:
  print(rps_list[rps])
  
  rand_computer = random.randint(0,2)
  computer_choose = rps_list[rand_computer]
  print(f"Computer chose: {computer_choose}")

  if(computer_choose == rock):
    if(rps == 0): #rock
      print("It's a tie.")
    elif (rps == 1): #paper
      print("You won!")
    elif(rps == 2): #scissors
      print("You lost.")
  elif(computer_choose == paper):
    if(rps == 0): #rock
      print("You lost.")
    elif (rps == 1): #paper
      print("It's a tie.")
    elif(rps == 2): #scissors
      print("You won!")
  else: #computer_choose == scissors 
    if(rps == 0): #rock
      print("You won!")
    elif (rps == 1): #paper
      print("You lost.")
    elif (rps == 2): #scissors
      print("It's a tie.")
