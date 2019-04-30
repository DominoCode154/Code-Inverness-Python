import random

MasterNumList = []
ImputList = []
VerdictList = []

print ("Welcome to MasterMind, my friend!")

for r in range(4):
    MasterNumList.append(random.randint(1,8))

#for q in MasterNumList:
 #   print (q) #Temporary for Testing and debug

print ("If a number is right, % appears. If a number is nearly right, ? appears. If a number is wrong, < appears.")

while ImputList != MasterNumList:
    ImputList = []
    VerdictList = []

    while len(ImputList) != len(MasterNumList):
        TempGuessImput = input("Pick a number between 1-8: ")
        try:
            ImputList.append(int(TempGuessImput))
        except ValueError:
            print ("That guess isn't valid...!")
            continue

    #for x in ImputList:
     #   print(x)

    #change output from guesses
    if ImputList[0] == MasterNumList[0]:
        VerdictList.append("%")
    else:
        if ImputList[0] == MasterNumList[1] or ImputList[0] == MasterNumList[2] or ImputList[0] == MasterNumList[3]:
            VerdictList.append("?")
        else:
            VerdictList.append("<")
    if ImputList[1] == MasterNumList[1]:
        VerdictList.append("%")
    else:
        if ImputList[1] == MasterNumList[0] or ImputList[1] == MasterNumList[2] or ImputList[1] == MasterNumList[3]:
            VerdictList.append("?")
        else:
            VerdictList.append("<")
    if ImputList[2] == MasterNumList[2]:
        VerdictList.append("%")
    else:
        if ImputList[2] == MasterNumList[1] or ImputList[2] == MasterNumList[0] or ImputList[2] == MasterNumList[3]:
            VerdictList.append("?")
        else:
            VerdictList.append("<")
    if ImputList[3] == MasterNumList[3]:
        VerdictList.append("%")
    else:
        if ImputList[3] == MasterNumList[0] or ImputList[3] == MasterNumList[2] or ImputList[3] == MasterNumList[1]:
            VerdictList.append("?")
        else:
            VerdictList.append("<")

    print (VerdictList)

print("You won! Thanks for playing MasterMind, my friend!")
