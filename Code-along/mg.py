
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