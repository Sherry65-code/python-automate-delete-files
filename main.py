import os 

os.system("whoami > .username.txt")

fr = file(".username.txt", "r")
usrname = fr.read().strip()
fr.close()

os.remove(".username.txt")

file_path = f'/users/{usrname}/Downloads/FILE PATH'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted!")
else:
    print("This file does NOT exist!!!")
