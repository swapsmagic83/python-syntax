def print_word(words):
    for word in words:
        print(word.upper())
        
           

def print_special_word(words):
    for word in words:
        if word[0].lower() == "e":
            print(word.upper())


def print_letters_word(words,letters):
    for word in words:
        for letter in letters:
            if word[0] == letter:
                    print(word.upper())