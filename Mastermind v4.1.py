import random

RandNumList = []
GuessList = []
VerdictList = []

print ("Welcome to MasterMind, my friend!")

for r in range(4):
    RandNumList.append(random.randint(1,8))

#for q in RandNumList:
 #   print (q) #Temporary for Testing and debug

print ("If a number you guess is right, % appears. If a number you guess is nearly right, ? appears. If a number you guess is wrong, < appears.")

while GuessList != RandNumList:
    GuessList = []
    VerdictList = []

    while len(GuessList) != len(RandNumList):
        TempGuessImput = input("Pick a number between 1-8: ")
        try:
            GuessList.append(int(TempGuessImput))
        except ValueError:
            print ("That guess isn't valid...!")
            continue

    #for x in GuessList:
     #   print(x)

    #change output from guesses
    if GuessList[0] == RandNumList[0]:
        VerdictList.append("%")
    else:
        if GuessList[0] == RandNumList[1] or GuessList[0] == RandNumList[2] or GuessList[0] == RandNumList[3]:
            VerdictList.append("?")
        else:
            VerdictList.append("<")
    if GuessList[1] == RandNumList[1]:
        print ("%")
    else:
        if GuessList[1] == RandNumList[0] or GuessList[1] == RandNumList[2] or GuessList[1] == RandNumList[3]:
            print ("?")
        else:
            print ("<")
    if GuessList[2] == RandNumList[2]:
        print ("%")
    else:
        if GuessList[2] == RandNumList[1] or GuessList[2] == RandNumList[0] or GuessList[2] == RandNumList[3]:
            print ("?")
        else:
            print ("<")
    if GuessList[3] == RandNumList[3]:
        print ("%")
    else:
        if GuessList[3] == RandNumList[0] or GuessList[3] == RandNumList[2] or GuessList[3] == RandNumList[1]:
            print ("?")
        else:
            print ("<")

    print (VerdictList)

print("You won! Thanks for playing MasterMind, my friend!")
