from pathlib import Path
import os
import datetime

def _cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

new_Folder = "OrganizadorDeArquivos"

path = "C:\\Users\\paulo.oliveira\\Desktop\\Python\\Teste"

_cleanScreen()

print(f"Default directory: {path}")

option_input = input(f"Do you want to change the directory? (y/n)").lower().strip()

while(option_input not in ['y', 'n']):

    option_input = input(f"Invalid option! Do you want to change the directory? (y/n)").lower().strip()

if(option_input == 'y'):
    
    path = input(f"""Type the new directory path: 
                 Exemple: {os.getcwd()}""").strip()
    
    if(os.path.exists(path) is True):

        print(f"Path {path} found!")

    else:

        while(os.path.exists(path) is False):
        
            print(f"Path {path} does not exists!")
            path = input(f"""Type the new directory path: 
                Exemple: {os.getcwd()}""").strip()
        

os.chdir(path)
print(f"Current folder: {os.getcwd()}")


if(not os.path.exists(new_Folder)):
    
    os.mkdir(new_Folder)
    print(f"Folder {new_Folder} created sucessfully!")

else:
    
    print(f"Folder {new_Folder} already exists.")

for files in os.listdir():
    
    print(files)
    
    if os.path.isfile(files):

        extension = files.split(".")[-1]

        if ("." in files):

            if(not os.path.exists(f"{new_Folder}//{extension}")):

                os.mkdir(f"{new_Folder}//{extension}")
                print(f"Folder {extension} created sucessfully!")

            else:

                print(f"Folder {extension} already exists.")    
            
            os.replace(files, f"{new_Folder}/{extension}/{files}")
            print(f"File {files} moved to folder {extension} successfully!")
    
    
