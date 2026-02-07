from caesar_cipher_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_true = True

while is_true:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    text = input("Type your message:\n").lower()
    
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    
    def caesar(text, shift, direction):
        
        if direction.lower() == 'encode':
            cipher_text = ""
            for char in text:
                if char.isalpha():
                    text_index = alphabet.index(char)
                    cipher_index = text_index + shift
                    cipher_text+= alphabet[cipher_index]
                else:
                    cipher_text+= char
            print(f"Here's the encoded result: {cipher_text}")
        
        elif direction.lower() == 'decode':
            plain_text = ""
            for char in text:
                if char.isalpha():
                    text_index = alphabet.index(char)
                    plain_index = text_index - shift
                    plain_text+= alphabet[plain_index]
                else:
                    plain_text+= char
            print(f"Here's the decoded result: {plain_text}")

    caesar(text=text, shift=shift, direction=direction)

    restart = input("Do you want to go again? Type 'yes' to continue, or 'no' to quit:\n")
    if restart.lower() != 'yes':
        is_true = False
        print("Goodbye")
        break