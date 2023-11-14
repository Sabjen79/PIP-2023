import os
import sys

try:
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments")
    
    directory = sys.argv[1]

    if not os.path.exists(directory):
        raise Exception("Directory not found")

    files = os.listdir(directory)
    extensions = {}

    for file in files:
        ext = file[file.rfind("."):]
        
        if ext in extensions:
            extensions[ext] += 1
        else:
            extensions[ext] = 1

    print(extensions)
        

except Exception as e:
    print(f"Error: {e}")