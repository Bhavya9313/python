import random
easy_word = ["apple","banana","train","tiger","monkey"]
medium_word = ["python","bottle","monkey","planet","laptop"]
hard_word = ["elephant","dimond","umbrella","computer","mountain"]
print("welcome to the password guessing game")
print("choose a defficulty level: easy,medium or hard")
level = input("enter difficulty: ").strip().lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)
elif level == "hard":
    secret = random.choice(hard_word)
else:
    print("invalid choice. Defaulting to easy level")
    secret = random.choice(easy_word)

attempts = 0
print(" guess the secret password")

while True:
    guess = input("enter your guess:").lower()
    
    if guess == secret:
        print("congratulations! you guessed it in", (attempts) ,"attempts.")
        break
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i]==secret[i]:
            hint += guess[i]
        else:
            hint +="_"
            attempts +=1

    print("hint:",hint)
print("game over")
