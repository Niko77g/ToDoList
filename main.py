import datetime

def readtodolist():
    with open("FileFolder/datafile.txt","r") as  file:
        for line in file:
            print(line, end="\n")
    
while True:
   valueofinput = input("Zadaj instrukciu, ktoru chces vykonat: ")
   if valueofinput == "r":
        readtodolist()
   elif valueofinput == "q":
        print("ukoncujem program")
        break
   else: 
        print("Neplatny vstup!")
