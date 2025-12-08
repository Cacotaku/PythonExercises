from pathlib import Path
import os
import datetime

def _apagarTela(): ### function to clean screen
    os.system('cls' if os.name == 'nt' else 'clear') 
    pass

_apagarTela() ### clean screen

new_Folder = "TextFilesTest" ### specify the name of the new folder

if(not os.path.exists(new_Folder)):

    os.mkdir(new_Folder) ### create the new folder
    print(f"Folder {new_Folder} created successfully!") ### print confirmation message

else:

    print(f"Folder {new_Folder} already exists.") ### print message if folder already exists

p = Path("NewFile.txt") ### specify the path of the new file

if(p.is_file() is False):

    new_File = open("NewFile.txt", "x") ### create a new file
    print(f"File {p} created successfully!") ### print confirmation message
    dateTime = datetime.datetime.now() ### get the current date and time    
    
    with open("NewFile.txt", "w") as write_File: ### open the file in append mode   
    
        write_File.write(f"Arquivo criado em: {dateTime} ###\n") ### write some text with date to the file
        print(f"Text added to file {p} sucessfully!") ### print confirmation message

else:

    dateTime = datetime.datetime.now() ### get the current date and time
    write_File = open("NewFile.txt", "a") ### open the file in write mode
    print(f"File {p} already created.") ### print message if file already exists
    
    with open("NewFile.txt", "a") as write_File: ### open the file in append mode   
    
        write_File.write(f"Adicionando texto no arquivo: {dateTime} ###\n") ### write some text with date to the file
        print(f"Text added to file {p} sucessfully!") ### print confirmation message

path = p.parent.absolute() ### get the absolute path of the file
print(p.is_file())
print(path)
print(path.is_dir())

otherPath = Path("C:/Users/paulo.oliveira/Desktop/Python/TextFilesTest")
print(otherPath.is_dir())
