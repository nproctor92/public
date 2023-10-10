import pandas as pd
import csv
import random
file = open('clean_wordlist.csv','r')
temp = list(csv.reader(file,delimiter=","))
cleaned = [i[0] for i in temp]

def hangman():
    game = 1
    stage = {
        0:"  __  \n |    \n |     \n |     \n_|____",
        1:"  __  \n |  o \n |     \n |     \n_|____",
        2:"  __  \n |  o \n |  0  \n |     \n_|____",
        3:"  __  \n |  o \n | /0  \n |     \n_|____",
        4:"  __  \n |  o \n | /0\ \n |     \n_|____",
        5:"  __  \n |  o \n | /0\ \n |  /  \n_|____",
        6:"  __  \n |  o \n | /0\ \n |  /\ \n_|____"
    }
    source = " "
    while source[0] != "1" and source[0] != "2": 
        source = input("What is the source of your word? \n 1 - inputting your own \n 2 - random from wordlist \n")
    if source[0]=="1":
        temp = input("What is your word? ")
        word = temp.upper()
    else:
        index = random.randrange(7655)
        word = cleaned[index].upper()
        
    counter = 0
    filt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    lstword = [i for i in word if i in filt]
    turn = 0
    used = []
    size = len(word)
    puzzle = []
    for i in lstword:
        if i==" ":
            puzzle.append(" ")
        else:
            puzzle.append("_")
    outstring = " ".join(puzzle)
    vic = "N"
    loss = "N"
    while game == 1:
        if turn == 0: print(f"Welcome! your word is {size} letters long")
        turn +=1
        tempguess = ""
        while tempguess == "":
            tempguess = input("What is your guess? ")
        guess = tempguess[0].upper()
        matches = [i for i in range(len(lstword)) if lstword[i]==guess]
        if guess not in used and len(matches)>0:
            for i in matches: puzzle[i] = lstword[i]
            used.append(guess)
            outstring = " ".join(puzzle)
            noose = stage[counter]
            sizm = len(matches)
            print(f"\n{guess} has {sizm} matches. \n word: {outstring} \n letters used: {used} \n{noose} \n misses: {counter}/6")
            if outstring.count("_")==0: vic = "Y"
        elif guess in used:
            print(f"\nYou have already tried {guess}")
        elif guess not in used and len(matches)==0:
            used.append(guess)
            counter+=1
            outstring = " ".join(puzzle)
            noose = stage[counter]
            print(f"\n{guess} has 0 matches. \n word: {outstring} \n letters used: {used} \n{noose} \n misses: {counter}/6")
            if counter == 6: loss = "Y"
        else:
            print("*loud farting noises*")
        if loss == "Y" or vic == "Y": game = 0
    if vic == "Y": print(f"Congratulations! You won! You correctly guessed {word}")
    if loss == "Y": print(f"Unfortunately, you lost. You failed to guess {word} \n{noose}")
repeat = "0"
while repeat == "0":
    init = input("Would you like to play Hangman? \n 1 - Yes \n 2 - No \n")
    if init[0]=="1":
        hangman()
    else:
        print("Goodbye")
        repeat = "1"
    

