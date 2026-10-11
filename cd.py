import os
import sys
import subprocess
request = sys.argv[1]

path = "error"

if request == '\\' or request == '/':
    drive = os.path.splitdrive(os.getcwd())[0]
    path = drive + "\\"

elif request == '..':
    path = os.path.dirname(os.getcwd())

else:
    if not os.path.isdir(request):
        path = "error"
    else:
        path = request

subprocess.run([os.path.dirname(__file__) + "\\cd.bat", path, "back"])

