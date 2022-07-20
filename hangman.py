import os
import random
file = open('words.txt', 'r')

lst = [] # Filling lst with words from file
for l in file:
    lst.append(l.rstrip()) # stripping the \n that is on each line and appending the word to the list

hiddenword = random.choice(lst) # Random picking word
#hiddenword = random.randint(0, len(lst) - 1) #Other way of doing it

hidden = '-' * len(hiddenword)

correctpicks = set()
strr = ''
life = 7
pick = ''
pickedletters = []


draw1 = """#############
#
#
#
#
#
#
#
#
#
#
#
#
#
#
###########################"""

draw2 = """#############
#           #
#           #
#
#
#
#
#
#
#
#
#
#
#
#
###########################"""

draw3 = """#############
#           #
#           #
#          ###
#          ###
#          ###
#
#
#
#
#
#
#
#
#
###########################"""

draw4 = """#############
#           #
#           #
#          ###
#          ###
#          ###
#           #
#         ###
#         # 
#         # 
#
#
#
#
#
###########################"""

draw5 = """#############
#           #
#           #
#          ###
#          ###
#          ###
#           #
#         #####
#         #   #
#         #   #
#
#
#
#
#
###########################"""

draw6 = """#############
#           #
#           #
#          ###
#          ###
#          ###
#           #
#         #####
#         # # #
#         # # #
#           # 
#
#
#
#
###########################"""

draw7 = """#############
#           #
#           #
#          ###
#          ###
#          ###
#           #
#         #####
#         # # #
#         # # #
#           # 
#          ##
#          # 
#          # 
#
###########################"""


draw8 = """#############
#           #
#           #
#          ###
#          ###
#          ###
#           #
#         #####
#         # # #
#         # # #
#           # 
#          ###
#          # #
#          # #
#
###########################"""

def letterin():
    global strr
    global life
    global pick
    global pickedletters
    global letter
    strr = ''
    letter = input('Enter one letter only: ')
    if len(letter) > 1 :
        return 'One letter only please'
    elif letter in pickedletters: # Checking if letter in picked letters
        return 'Please choose a new letter '

    pickedletters.append(letter) # Trying to store previous selections

    pick = letter

    if letter in hiddenword:
        correctpicks.add(letter)


        for char in hiddenword:
            if char not in correctpicks:
                strr += '-'
            elif char in correctpicks:
                strr += char



        return 'That is correct' + ' ' + strr


    elif letter not in hiddenword:
        life -= 1
        for char in hiddenword:
            if char not in correctpicks:
                strr += '-'
            elif char in correctpicks:
                strr += char
        return 'Not in word +1 limb ' + strr
def drawman(life):
    if life == 6:
        print(draw2)
    elif life == 5:
        print(draw3)
    elif life == 4:
        print(draw4)
    elif life == 3:
        print(draw5)
    elif life == 2:
        print(draw6)
    elif life == 1:
        print(draw7)
    elif life == 0:
        print(draw8)







if __name__ == '__main__':
    while strr != hiddenword and life > 0:
        os.system('cls')
        drawman(life)
        
        if pick not in hiddenword:
            print(f'{pick} Not in the word +1 limb ' + strr) 
        else:
            print(strr)
        print(letterin())
    if strr == hiddenword:
        print('You have found the right word! ')
    elif life == 0:
        print(f'You Lose, the correct word was {hiddenword}')