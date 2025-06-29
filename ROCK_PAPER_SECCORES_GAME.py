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

user_choice = input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors: ")

if user_choice == "0" or user_choice == "1" or user_choice == "2":
    if user_choice == "0":
        user_choice = rock
    elif user_choice == "1":
        user_choice = paper
    elif user_choice == "2":
        user_choice = scissors

    options = [rock, paper, scissors]
    computer_choice = random.choice(options)

    print(user_choice)
    print(f"computer chose\n{computer_choice}")

    if computer_choice == user_choice:
        print("It's a draw!")
    elif computer_choice == rock and user_choice == paper:
        print("you win!")
    elif computer_choice == scissors and user_choice == rock:
        print("you win!")
    elif computer_choice == rock and user_choice == paper:
        print("you win!")
    elif computer_choice == rock and user_choice == scissors:
        print("you lose!")
    elif computer_choice == paper and user_choice == rock :
        print("you lose!")
    elif computer_choice == scissors and user_choice == paper:
        print("you lose!")

else:
    print("invalid choice")