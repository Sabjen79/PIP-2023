import os
import sys

try:
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments")
    
    directory = sys.argv[1]

    if not os.path.exists(directory):
        raise Exception("Directory not found")

    files = os.listdir(directory)

    for index, file in enumerate(files):
        path = os.path.join(directory, file)
        new_file = f"file{index+1}{os.path.splitext(file)[1]}"
        new_path = os.path.join(directory, new_file)

        try:
            os.rename(path, new_path)

        except Exception as e:
            print(f"Can't rename file: {file}: {e}")

except Exception as e:
    print(f"Error: {e}")