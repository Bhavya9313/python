import random
item_list = ["r","p","s"]

user_choise = input("enter your move \nfor rock-r\nfor paper-p,\nfor scissor-s").lower()
comp_choise = random.choice(item_list)
print(f"user choice = {user_choise},computer choice {comp_choise}")
    
if user_choise == comp_choise:
    print("both chooses same: match tie")


elif user_choise == "r":
    if comp_choise == "p":
        print("paper covers rocks! computer win")
    
    else:   
        print("rock smashes scissor! you win")
    
elif user_choise == "p":
    if comp_choise == "s":
        print("scissor cuts paper! computer win")
    
    else:
        print("paper covers rock! you win")
    
elif user_choise == "s":
    if comp_choise == "p":
        print("scissor cuts paper! you win")
        
    else:
        print("rock smashes scissor! computer win")



    
