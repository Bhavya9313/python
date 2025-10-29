# in this we are deliver or recive a message in a encryption or in decryption
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key): #HELLO H=7
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos+shift_key)%26  #used for after 26 word
            cipher_text +=alphabet[new_pos]
        else:
            cipher_text += char 
    print(f"here is the text after encryption {cipher_text}")

def decryption(cipher_text,shift_key): #khoor
    plain_text = ""
    for char in cipher_text: #char=k
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos-shift_key)%26  #used for after 26 word
            plain_text +=alphabet[new_pos]
        else:
            plain_text += char
    print(f"here is the text after decryption {plain_text}")

while True:
    type = input("type 'encrypt' for encryption , type 'decrypt' for decryption" )
    text = input("type your message").lower()
    shift = int(input("enter shift key:\n")) 
    if type == "encrypt":
        encryption(text,shift)
    elif type == "decrypt":
        decryption(text,shift)
    
    play_again = input("type 'yes' to continue, type'no' to exit" )
    if play_again == "no":
         break
    print("have a nice day bye...")
