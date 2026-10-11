import os
import sys

path = sys.argv[1]

if not os.path.isfile(path):
    print(f"the file {path} does not exist")
    sys.exit(1)

with open(path, "rb") as f:
    data = f.read()

i = 0
while i < len(data):
    chunk = data[i:i + 16]

    line = ""
    for b in chunk:
        line += format(b, "02x") + " "

    print(line.strip())
    i += 16