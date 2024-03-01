import datetime

def readtodolist():
    with open("FileFolder/datafile.txt","r") as  file:
        for line in file:
            print(line, end="\n")
def addtodolist():
    with open("FileFolder/datafile.txt","a") as  file:
        new_content = input("Zadaj novy todolist: ")
        file.write(new_content + "\n")
        print("Pridavam novy todolist")
    readtodolist()
    
while True:
   valueofinput = input("Zadaj instrukciu, ktoru chces vykonat: ")
   if valueofinput == "r":
        readtodolist()
   elif valueofinput == "a":
       addtodolist()
   elif valueofinput == "q":
        print("ukoncujem program")
        break
   else: 
        print("Neplatny vstup!")
