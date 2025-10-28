#in this game we chose a correct word
import random
word_list = ["apple","mango","banana"]
lives = 6
chosen_word = random.choice(word_list)
print("you have only 6 moves")
print("chose only fruits name")

display = []
for i in range(len(chosen_word)):
    display +="_"
print(display)


while True:
    guessed_letter = input("guess a latter").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -=1
        print(f"now you have only {lives} lives")
        if lives==0:
            print("you lose!")
            break
    if '_' not in display:
        print("you win!")
        break



