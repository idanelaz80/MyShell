import subprocess
import os
import getpass

pathD = os.path.dirname(os.path.abspath("shell.py"))


while True:
    print(pathD+">>>",end = "")
    com = input()
    com = com.lower()
    if com == "exit":
        break
    if com == "hello":
        print("Hello" + getpass.getuser())
    if com == "ls" or com.startswith("ls "):
        parts = com.split()
        if len(parts) > 1:
            path = parts[1]
        else:
            path = pathD
        subprocess.run(["ls.bat", path])
    if com.startswith("grep "):
        parts = com.split()
        if len(parts) > 2:
            string = parts[1]
            path = parts[2]
            subprocess.run(["grep.bat", string, path])
        else:
            print("parameters missing")



