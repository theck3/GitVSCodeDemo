import random

target = random.randint(1, 100)
guess = 0

# loop to take guess input from user and decide if it is higher or lower than target

while guess != target:
    guess = int(input("Take a guess: "))
    if guess > target:
        print("Your guess is too high. Try again. ")
    elif guess < target:
        print("Your guess is too low. Try again. ")

print("Congratulations, you guessed correctly!")
