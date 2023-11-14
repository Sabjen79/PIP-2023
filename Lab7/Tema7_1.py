import os
import sys

if len(sys.argv) < 3:
    raise Exception("Not enough arguments.")

try:
    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.exists(directory):
        raise Exception("Directory not found")

    if not extension.startswith("."):
        raise Exception("Invalid file extension format. It should start with '.'")

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)

            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"File: {filename}\nContent:\n{content}\n")

            except Exception as e:
                print(f"Error reading file {filename}: {e}")

except Exception as e:
    print(f"Error: {e}")