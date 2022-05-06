import random
import csv

with open('list_of_words.csv', 'r', encoding='utf8', newline='\r\n') as file:
    data_file = csv.reader(file)
    data = list(data_file)
    list_data = random.choice(data)
word = random.choice(list_data)
list_word = list(word)
word_letters = list(set(word))


print("____________HANGMAN____________")
print(" +---+\n |   |\n     |\n     |\n     |\n     |\n========", '\n')
#print(word_letters)
#print(list_word)

error0_img = " +---+\n |   |\n     |\n     |\n     |\n     |\n========"
error1_img = " +---+\n |   |\n O   |\n     |\n     |\n     |\n========"
error2_img = " +---+\n |   |\n O   |\n |   |\n     |\n     |\n========"
error3_img = " +---+\n |   |\n O   |\n/|   |\n     |\n     |\n========"
error4_img = " +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n========"
error5_img = " +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n========"
error6_img = " +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n========"

error_list_img = [error0_img, error1_img, error2_img, error3_img, error4_img, error5_img, error6_img]
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


if correct_attempts == count_word_letters:
    print("\n\nYOU WIN! \nCongratulations!")
else:
    print("\n\nGAME OVER! \nTRY AGAIN")


# fixme: despúes al final errores en caso que tipee algo que no sea letra
#  o mas de una letra junta, o mas de una vez la misma letra
# todo ver ultimos dos videos del lab 03 en cap 05 porque da una mano de como empezar con las clases