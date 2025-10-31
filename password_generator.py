import random
letters = ['a','b','c','d','e','f','g','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','&','.',',','*','+']
print("welcome to password generator")
n_letters = int(input("how many letters you want in your passwoord?\n"))
n_symbols = int(input("how many symbols you want in your passwoord?\n"))
n_numbers = int(input("how many numbers you want in your passwoord?\n"))
password =[]
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password += char

for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password += char

for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password += char

print(password)
random.shuffle(password)
print(password)

pswd = ""
for i in password:
    pswd += char
print(pswd)
 