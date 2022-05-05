import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99\
 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

value = random.randint(1, 99)
attempts = 0
while True:
    print("What's your guess between 1 and 99?")
    guess = input(">> ")
    if guess == "exit":
        print("Goodbye!")
        break
    try:
        guess = int(guess)
        if guess < value:
            print("Too low!")
        elif guess > value:
            print("Too high!")
        else:
            if value == 42:
                print("The answer to the ultimate question of life,\
 the universe and everything is 42.")
            if attempts == 0:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in %d attempts." % (attempts + 1))
            break
    except ValueError:
        print("That's not a number.")
    attempts += 1
