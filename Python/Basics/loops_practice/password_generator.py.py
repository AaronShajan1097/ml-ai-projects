#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

random_letters = []
for _ in range(nr_letters):
    rand_num_let = random.randint(0, len(letters) - 1) 
    rand_let = letters[rand_num_let]
    random_letters.append(rand_let)

random_numbers = []
for _ in range(nr_numbers):
    rand_num_num = random.randint(0, len(numbers) - 1)
    rand_num = numbers[rand_num_num]
    random_numbers.append(rand_num)

random_symbols = []
for _ in range(nr_symbols):
    rand_num_sym = random.randint(0, len(symbols) - 1) 
    rand_sym = symbols[rand_num_sym]
    random_symbols.append(rand_sym)
#----------------------------------
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# joined_letters = ''.join(random_letters)
# joined_numbers = ''.join(random_numbers)
# joined_symbols = ''.join(random_symbols)

#print(f"{joined_letters}{joined_numbers}{joined_symbols}")

#----------------------------------
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

combined_characters = random_letters + random_numbers + random_symbols

random.shuffle(combined_characters)

password = ''.join(combined_characters)

print(f"{password}")