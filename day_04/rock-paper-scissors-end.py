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

computer_choise = random.randint(0, 2)
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choise >= 3 or user_choise < 0:
    print("Invalid number!! You Loose")
    
else:
    print(options[user_choise])
    print(f"Computer choose: \n {options[computer_choise]}")

    # row -> user_choise | column -> computer_choise
    # [0,0] [0,1] [0,2]
    # [1,0] [1,1] [1,2]
    # [2,0] [2,1] [2,2]
    
    win_metric = [["draw", "loose", "win"], 
                  ["win", "draw", "loose"], 
                  ["loose", "win", "draw"]]
    
    print(win_metric[user_choise][computer_choise])





