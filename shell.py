import subprocess
import os
import getpass
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
pathD = os.getcwd()

while True:
    print(pathD+">>>",end = "")
    inp = input()
    com = inp.lower()

    if com == "exit":
        break

    elif  com == "hello":
        print("Hello " + getpass.getuser())

    elif  com == "ls" or com.startswith("ls "):
        parts = com.split()
        if len(parts) > 1:
            path = parts[1]
        else:
            path = pathD
        subprocess.run([os.path.join(HERE, "ls.bat"), path], cwd=pathD)

    elif  com.startswith("grep "):
        parts = com.split()
        if len(parts) > 2:
            string = parts[1]
            path = parts[2]
            subprocess.run([os.path.join(HERE, "grep.bat"), string, path], cwd=pathD)
        else:
            print("parameters missing")

    elif  com.startswith("hexdump "):
        path = com[8:].strip().strip('"')
        subprocess.run([os.path.join(HERE, "hexdump.bat"), path], cwd=pathD)

    elif com.startswith("cd "):
        parts = com.split()
        request = com[2:].strip().strip('"')
        result = subprocess.run([os.path.join(HERE, "cd.bat"), request],capture_output=True, encoding="oem", cwd=pathD)
        ans = result.stdout.strip()
        if ans != "error":
            pathD = ans
        else:
            print("File does not exists")

    else:
        print("not a vaild command")








