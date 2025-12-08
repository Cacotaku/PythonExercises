from pathlib import Path
import os
import datetime

def _cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

new_Folder = "OrganizadorDeArquivos"

path = "C:\\Users\\paulo.oliveira\\Desktop\\Python\\Teste"

print("Original Folder: ", os.getcwd())
os.chdir(path)
print("Current folder: ", os.getcwd())


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
                print("tsete")
                print(f"Folder {extension} created sucessfully!")
            #os.replace(files, f"{new_Folder}/{extension}/{files}")
            #print(f"File {files} moved to folder {extension} successfully!")
            else:
                print(f"Folder {extension} already exists.")    
