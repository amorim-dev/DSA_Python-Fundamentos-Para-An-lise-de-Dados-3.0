# Hangman Game with PPO
# By Bianca Amorim

# Import
import random

# Board
print("____________HANGMAN____________")
print(" +---+\n |   |\n     |\n     |\n     |\n     |\n========", '\n')
error0_img = " +---+\n |   |\n     |\n     |\n     |\n     |\n========"
error1_img = " +---+\n |   |\n O   |\n     |\n     |\n     |\n========"
error2_img = " +---+\n |   |\n O   |\n |   |\n     |\n     |\n========"
error3_img = " +---+\n |   |\n O   |\n/|   |\n     |\n     |\n========"
error4_img = " +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n========"
error5_img = " +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n========"
error6_img = " +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n========"
error_list_img = [error0_img, error1_img, error2_img, error3_img, error4_img, error5_img, error6_img]

# todo: Class, ver despues el nombre de todas las variables para coincidir con los que fui poniendo
class Hangman:
    # Constructor method
    def __init__(self, word):

    # method to guess the letter
    def gues(self, letter):

    # method to check if the game has ended
    def hangman_over(self):

    # method to check if the player has won
    def hangman_won(self):

    # method to not showing the letter on the board
    def hide_word(self):

    # method to check the game status and print the board
    def print_game_status(self):


# function to read a random word in the list of words (See if I have to use this, because I did different) todo: listo
# strip - Remove spaces before and after the word
def rand_word():
    with open("list_of_words.txt", "r") as f:
        bank = f.readlines()
    return bank[random.randint(a,len(bank))].strip()

# Main Function - program execution
def main():
    # objeto
    game = Hangman(rand_word())

    # While the game is not finished, print the status, request a letter and read the character

    # Check the status game
    game.print_game_status()

    # According to the status, prints a message on the screen for the user
    if game.hangman_won():
        print("\nCongratulations! You won!")
    else:
        print("\nGame over!")
        print("The word was " + game_word)

    print("It was nice playing with you! Now go to study\n")

# executes the program
if __name__ =="__main__":
    main()


correct_letters = []
wrong_letters = []
underlines_list = []

correct_attempts = 0
wrong_attempts = 0
count_word_letters = len(word_letters)

for i, word_letter in enumerate(list_word):
    underlines_list.append('_')

while wrong_attempts < 6 and correct_attempts < count_word_letters:
    letter = input("\n\nType one letter: ")
    found_letter = False
    for i, word_letter in enumerate(word):
        if word_letter == letter:
            found_letter = True
            underlines_list[i] = letter

    if found_letter:
        correct_letters.append(letter)
        correct_attempts += 1
    else:
        wrong_letters.append(letter)
        wrong_attempts += 1

    for i in error_list_img:
        if error_list_img.index(i) == wrong_attempts:
            print(i)

    print("\nWrong letters: ", wrong_letters)
    print("Correct letters: ", correct_letters)

    print('\nWord: ')
    for word_letter in underlines_list:
        print(word_letter, end='')


# fixme: despúes al final errores en caso que tipee algo que no sea letra
#  o mas de una letra junta, o mas de una vez la misma letra
