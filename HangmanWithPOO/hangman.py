# Hangman Game with PPO
# By Bianca Amorim

# Import
import random

# Board
error_list_board = ['''

____________HANGMAN____________

 +---+
 |   |
     |
     |
     |
     |
======== ''', '''
 
 +---+
 |   |
 O   |
     |
     |
     |
========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
========''', '''

 +---+
 |   |
 O   |
/|\\ |
     |
     |
========''', '''

 +---+
 |   |
 O   |
/|\\ |
/    |
     |
========''', '''

 +---+
 |   |
 O   |
/|\\ |
/ \\ |
     |
========''']


# Class
class Hangman:

    # Constructor method
    def __init__(self, word):
        self.word = word
        self.correct_attempts = 0
        self.wrong_attempts = 0
        self.correct_letters = []
        self.wrong_letters = []
        self.underline_list = ''

    # method to guess the letter
    def guess(self, letter):
        if letter in self.word and letter not in self.correct_letters:
            self.correct_letters.append(letter)
            self.correct_attempts += 1
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
            self.wrong_attempts += 1

    # method to check if the game has ended
    def hangman_over(self):
        if len(self.wrong_letters) == 6 or self.hangman_won():
            return True
        return False

    # method to check if the player has won
    def hangman_won(self):
        if self.underline_list == self.word:
            return True
        return False

    # method to show the letter on the board
    def show_underline(self):
        self.underline_list = ''
        for letter in self.word:
            if letter not in self.correct_letters:
                self.underline_list += '_'
            else:
                self.underline_list += letter

    # method to check the game status and print the board
    def print_game_status(self):
        for i in error_list_board:
            if error_list_board.index(i) == self.wrong_attempts:
                print(i)
        print("\nWord: ", self.underline_list)
        print("\nWrong letters: ", self.wrong_letters)
        print("Correct letters: ", self.correct_letters)


# function to read a random word in the list of words
# strip - Remove spaces before and after the word
def rand_word():
    with open("list_of_words.txt", "r") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Main Function - program execution
def main():
    # object
    game = Hangman(rand_word())

# While the game is not finished, print the status, request a letter and read the character
    while not game.hangman_over():
        game.print_game_status()
        user_letter = input("\n\nType one letter: ")
        game.guess(user_letter)
        game.show_underline()

    game.print_game_status()

    # According to the status, prints a message on the screen for the user
    if game.hangman_won():
        print("\nCongratulations! You won!")
    else:
        print("\nGame over!")
        print("The word was " + game.word)

    print("It was nice playing with you!\n")


# executes the program
if __name__ == "__main__":
    main()

