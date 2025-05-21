import random
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
game_images=[rock,paper,scissors]
user_input=int(input("What is your choice? write 0 for rock,1 for paper and 2 for scissors\n"))
computer_input=random.randint(0,2)
if 0<= user_input <=2:
    print("user's choice:\n")
    print(game_images[user_input])
    print("computer's choice:\n")
    print(game_images[computer_input])
    if user_input==2 and computer_input==0:
        print("You lose!")
    elif user_input==0 and computer_input==2:
        print("You win!")
    elif user_input > computer_input:
        print("you win!")
    elif computer_input > user_input:
        print("You lose!")
    elif user_input == computer_input:
        print("It's a Draw")
else:
   print ("You have entered an incorrect option")

