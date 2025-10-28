import os 
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}: created successfully!")
    except FileExistsError:
        print(f"File name {filename} already exists!")

    except Exception as e:
        print("an error occured")

def view_all_files():
    files = os.listdir()  # it returns all files list in which user exists
    if not files:
        print("no file found")
    else:
        print("files in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("file not exist")
    
    except Exception :
        print("an error occured!")

def read_file(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
            print(f"content of {filename}:\n{content}")
    except FileNotFoundError:
        print("file not exist")
    
    except Exception :
        print("an error occured!")

def edit_file(filename):
    try:
        with open(filename,"a") as f:  # yaha dekhna hai abhe
            content = input("enter dat ato add = ")
            f.write(content + "\n")
            print("content added to {filename} successfully!")

    except FileNotFoundError:
        print("file not exist")
    
    except Exception :  # yaha bhe dekhmna hai 
        print("an error occured!")

def main():
    while True:
        print("File managment app")
        print("1: Create file")
        print("2: View all file")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")
        choice = int(input("enter your choice(1-6)"))

        if choice == 1:
            filename = input("enter the file_name to create = ")
            create_file(filename)
        
        elif choice == 2:
            view_all_files()
        
        elif choice == 3:
            filename = input("enter the file name you want to delete ")
            delete_file(filename)
            
        elif choice == 4:
            filename == input("enter file name you want to read")
            read_file(filename)

        elif choice == 5:
            filename = input("enter file name you want to edit")
            edit_file(filename)
        
        elif choice == 6:
            print("EXIT")
            break
            
    
    else:
        print("invalid syntax")
        
main()
