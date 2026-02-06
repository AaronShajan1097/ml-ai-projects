import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabets = {row.letter:row.code for (index, row) in data.iterrows()}


is_true = True
while is_true:
    try:
        user_code = input("Enter a word: ").upper()
        if user_code.lower() == 'exit':
            break
        else:
            code = [nato_alphabets[char] for char in user_code]
            print(code)
            print()
    
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

    else:
        is_true = False