import os
import sys

direct = sys.argv[1]

if not os.path.isdir(direct):
    print(f"Folder not found: {direct}")
    sys.exit(1)

for name in os.listdir(direct):
    print(name)