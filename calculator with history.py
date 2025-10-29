history_file = "history.text"

def show_history():
    file = open(history_file,"r")
    lines = file.readlines()
    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file,"w")
    file.close()
    print("history cleared.")

def history_save(equation,result):
    file = open(history_file,"a")
    file.writelines(equation + "=" + str(result)+"/n")
    file.close()

def calculate(user_input):
    parts = user_input
    print(parts)
    if len(parts)!=3:
        print("invalid input. use format: e.g 8+8")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2

    elif op == "-":
         result = num1 - num2
  
    elif op == "*":
        result = num1 * num2
            
    elif op == "/":
        if num2 == 0:
            print("cannot devide by zeero")
            return
        result = num1 / num2
    else:
        print(f"invalid operator. use only + - / * except {op}")  
        return
    
    if int(result)== result:
        result = int(result)
    
    print("result",result)

    history_save(user_input,result)

def main():
    print("SIMPLE CALCULATOR (type history,clear or exit)")
    while True:
        user_input = input("enter calculation (+ - * /) or command(history, clear or exit)").strip().lower()
        if user_input == "exit":
            print("good bye")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()

     


