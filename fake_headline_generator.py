import random

subjects = [
    "akshay kumar",
    "Virat kohli",
    "A mumbai cat",
    "A group of monkey ",
    "pime minister modi"
]

actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "orders"
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "at india gate",
    "at ganga ghat",
    "a plate of samosa"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)
    headline = f" BREAKING NEWS: {subject} {action} {places_or_thing}"  #(forward string) is used to print 3 variables value in a single variable
    print("/n"+headline)
    user_input = input("/n do you want another headline? (yes/no)").strip().lower()

    if user_input == "no":
        break 
    if user_input != ("yes" or "no"):
        print("please enter (yes or no)")
        break

print("Good bye thanks for using the fake headline generator")

