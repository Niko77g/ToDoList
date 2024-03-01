import time
class Task:
    def __init__(self,name,priority):
        self.name = name
        self.priority = priority
def readtodolist():
    with open("FileFolder/datafile.txt","r") as  file:
        for line in file:
            print(line, end="\n")
    
def addtodolist():
    time_object = time.localtime()        
    local_time = time.strftime("(%B-%d-%Y)", time_object)
    new_content = input("Zadaj nový todolist: ")
    while True:
        priority = input("Zadaj prioritu danej úlohy (1-3): ")
        if priority in ["1", "2", "3"]:
            break
        else:
            print("Neplatný rozsah priority!")

    task = Task(new_content,int(priority))
    with open("FileFolder/datafile.txt", "a") as file:
        file.write(f"{local_time} [{task.priority}] {task.name} \n")
        print("Pridávam nový todolist")
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
