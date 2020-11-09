from random import randint

# Solution:
print("")
print('''
Welcome to the 'Rock Scissors Paper' game!

Game rules:
  Rock wins against scissors
  Scissors win against paper
  Paper wins against rock

''')

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
ai_choice = randint(0, 2)


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

# ======================

# Player choice:
if your_choice == 0:
  print('''You've chosen:
  ''')
  print(rock)
  print("")
  
if your_choice == 1:
  print('''You've chosen:
  
  ''')
  print(paper)
  print("")

if your_choice == 2:
  print('''You've chosen:
  
  ''')
  print(scissors)
  print("")


# AI choice:
if ai_choice == 0:
  print('''Computer chose:
  
  ''')
  print(rock)

elif ai_choice == 1:
  print('''Computer chose:
  
  ''')
  print(paper)
elif ai_choice == 2:
  print('''Computer chose:
  
  ''')
  print(scissors)

print("")

if your_choice == 0 and ai_choice == 2:
  print("You win!")
elif your_choice == 2 and ai_choice == 1:
  print("You win!")
elif your_choice == 1 and ai_choice == 0:
  print("You win!")
elif your_choice == ai_choice:
  print("Draw!")
else:
  print("You lose :(")
