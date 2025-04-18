#hangman
import random
from wordlist import words

art = {0:("  ",
          "  ",
          "  ",),
       1:(" o ",
          "   ",
          "   ",),
       2:(" o ",
          " | ",
          "   ",),
       3:(" o ",
          "/| ",
          "   ",),
       4:(" o ",
          "/|\\ ",
          "   ",),
       5:(" o ",
          "/|\\ ",
          "/   ",),
       6:(" o ",
          "/|\\ ",
          "/ \\  ",)}

def display_man(wrong_guess):
    for line in art[wrong_guess]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    wrong_guess = 0 #counter for displaying art
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    guessed_letter = set() #storage for guess
    is_running = True
#Starting program
    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Enter your guess letter: ").lower()
#Checking valid input (must be one input at a time and it should be no numbers)
        if len(guess) != 1 or guess.isdigit():
            print("Invalid input")
            continue
#Checking if the input has already gussed
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        guessed_letter.add(guess) #add the input to guessed storage
#core of this program
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i]=guess
        else:
            wrong_guess += 1
#Diplaying win
        if '_' not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU WON!!")
            is_running = False
#Displaying loss
        elif wrong_guess ==6:
            display_man(wrong_guess)
            display_answer(answer)
            print("You LOSE!!!")
            is_running = False


if __name__ == "__main__":
    main()