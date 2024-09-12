import random as rng
import time
attempts = 0
rng_number = rng.randint(1, 100)
ai_attempts = 0
i=0
while attempts < 10:
    user_input = rng.randint(1,100)

    while user_input != rng_number:

        i += 1
        print(i)
        user_input = rng.randint(1,100)

    
    print(user_input, rng_number)
    if user_input == rng_number:
        print("Du vann!")
        break
    elif rng_number - user_input < 10:
        print("du är nära (+-: 10)")
    elif rng_number - user_input < 7:
        print("du är nära (+-: 7)")
    elif rng_number - user_input < 5:
        print("du är nära (+-: 5)")
    elif rng_number - user_input < 3:
        print("du är nära (+-: 3)")
    else:
        print("inte nära.")
    if attempts == 10:
        print("du förlorade!")


