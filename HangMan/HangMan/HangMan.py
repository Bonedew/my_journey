import time


def greeting():
    print("Welcome to the hangman game.")
    time.sleep(2)
    print("Made by Ruuben Jalasto")

def get_word():
    time.sleep(2)
    under_12 = False
    while under_12 == False:
        temp_word = input("Input a word for the game(max letters 12): ")
        if len(temp_word) <= 12:
            return  temp_word
            under_12 = True
        else:
            print("You have entered more that 12 letters, try again.")
            time.sleep(2)
            continue

def get_letters():
    word_list = [] 
    num = 0
    while num < letter_count:  
        word_list.append(user_word[num])
        num += 1
    return word_list

def make_lines():
    i = 0
    line_list = []
    while i < letter_count:
        line_list.append("_")
        i += 1
    return line_list

def hang_man():
    game_active = True
    guesses = 0
    while game_active == True and guesses < 8:
        print("You have "+ str(8-guesses) + " guesses left.")
        print(guessing_list)
        time.sleep(2)
        guess = input("Guess a letter: ")
        if guess in user_word_list: 
            print("The letter " + guess + " is in the word.")
            i = 0
            for letter in user_word_list:
                if guess == letter:
                    guessing_list.pop(i)
                    guessing_list.insert(i, guess)
                    i += 1
                else:
                    i += 1
            print(guessing_list)
            solve_y = input("Would you like to solve?(Y/N)")
            if solve_y == "Y" or solve_y == "y":
                guessed_word = input("Guess the word: ")
                if guessed_word == user_word:
                    print("You guessed the word!")
                    game_active = False
                else:
                    continue


        else:
            print("Oops, try again")
            guesses += 1


def black_box():
    print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """)



greeting()
user_word = get_word()
letter_count = len(user_word)
user_word_list = get_letters()
guessing_list = make_lines()

black_box()
hang_man()


