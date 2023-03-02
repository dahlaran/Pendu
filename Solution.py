import random

# 40 minutes dont 15 de tests

max_lives = 10
listOfWords = ["Miam", "Eskimo", "Cou", "Porter", "Coussin", "Civile"]


def show_letters_found(list_of_find_letters):
    for letter in list_of_find_letters:
        print(letter, end=',')
    print()


def show_word(word, list_of_find_letters):
    print(list_of_find_letters)
    for letter in word:
        if list_of_find_letters.__contains__(letter.lower()):
            print(letter, end='')
        else:
            print("_", end='')
    print()


def is_finish(word, list_of_find_letters):
    for letter in word:
        if not list_of_find_letters.__contains__(letter.lower()):
            return False
    return True


def play():
    word = random.choice(listOfWords)
    list_of_find_letters = []
    show_word(word, list_of_find_letters)
    lives = max_lives
    while lives > 0 and not is_finish(word, list_of_find_letters):
        letter = input("Entrez une lettre :")
        if letter.__len__() == 1 and letter.isalpha():
            letter = letter.lower()
            if list_of_find_letters.__contains__(letter):
                print("La lettre existe déjà")
            else:
                list_of_find_letters.append(letter)
                if word.lower().__contains__(letter):
                    print("Oui")
                else:
                    lives = lives - 1
                    print("NoOOOO")
                print("Lives = " + str(lives) + "/" + str(max_lives))
                show_word(word, list_of_find_letters)
        else:
            print("Essaye une autre lettre")
    if is_finish(word, list_of_find_letters):
        print("BRAVO vous avez trouvé " + word)
    else:
        print("Dommage le mot était " + word)


play()
