import os
import sys

string = sys.argv[1]
file = sys.argv[2]

if not os.path.isfile(file):
    print(f"File not found: {file}")
    sys.exit(1)

with open(file, "r") as f:
    for num, line in enumerate(f, start=1):
        if string in line:
            print(f"{num}: {line.rstrip()}")

