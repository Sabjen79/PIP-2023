import os
import sys

try:
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments")
    
    directory = sys.argv[1]

    if not os.path.exists(directory):
        raise Exception("Directory not found")

    files = os.listdir(directory)
    bytes_count = 0

    for file in files:
        if os.path.isdir(file):
            files.append(os.listdir(file))
            continue

        
        bytes_count += os.path.getsize(os.path.join(directory, file))

    print(f"Size of all files: {bytes_count}")

except Exception as e:
    print(f"Error: {e}")