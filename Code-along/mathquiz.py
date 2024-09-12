# while True:
#     number1 = rng.randint(1, 10)
#     number2 = rng.randint(1, 10)
# 
#     user_answer = int(input(f"What is {number1} * {number2}"))
#     if user_answer == number1 * number2:
#         print("Correct!")
# 
#     else:
#         print(f"{user_answer} is wrong!")
# 
#     play_again = input("want to play again? (y/n)")
#     if play_again != "y":
#         print("Good bye!")
#         break

# import random as rng
# attempts = 0
# random_number = rng.randint(1, 100)
# while attempts < 10:
#     user_guess = int(input("Gissa siffran 1-100: "))
#     attempts += 1
#     if user_guess == random_number:
#         print(f"korrekt gissning! ({random_number})")
#     elif random_number - user_guess < 10:
#         print("Du är nära! försök igen")
#     elif random_number - user_guess < 5:
#         print("Du är jättenära! försök igen")
#     else:
#         print("försök igen.")

import random as rng

correctguesses = 0
difficulty1 = 10
difficulty2 = 100
difficulty3 = 1000

while True:
    try:
        ask_difficulty = int(input("Ange Svårigetsgrad: x10,x100,x1000 (1-3)"))
        if ask_difficulty == 1:
            difficulty = difficulty1
        elif ask_difficulty == 2:
            difficulty = difficulty2
        elif ask_difficulty == 3:
            difficulty = difficulty3
        else:
            print("felaktig inmatning, försök igen.")
        print("för att avsluta skrix 'x', för att byta svårighet skrix 'z'")
    except ValueError:
        print("felaktig inmatning.")
        continue
    while True:
        x = rng.randint(1, difficulty)
        y = rng.randint(1, difficulty)
        correct_answer = x * y
        print(f"vad blir {x} * {y}? ")
        user_guess = input("Ange ditt svar: ")
        if user_guess == 'z':
            break
        elif user_guess == 'x':
            exit()
        elif user_guess.isdigit() and int(user_guess) == correct_answer:
            print(f"Korrekt svar! {x} * {y} = {correct_answer} ")
        elif user_guess.isdigit() and int(user_guess) != correct_answer:
            print(f"Fel svar, det korrekta svaret är: {x*y}")
        else:
            print("Felaktig inmatning, 'x' för att avsluta 'z' för att byta svårighetsgrad")