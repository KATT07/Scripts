import os
import shutil

# source folder
source_folder = input("Enter source folder: ").strip()

# destination folder
destination_folder = input("Enter destination folder: ").strip()

# create destination if not exists
os.makedirs(destination_folder, exist_ok=True)

count = 0

for root, dirs, files in os.walk(source_folder):
    for file in files:
        source = os.path.join(root, file)
        destination = os.path.join(destination_folder, file)

        # avoid overwriting files with same name
        if os.path.exists(destination):
            name, ext = os.path.splitext(file)
            i = 1
            while os.path.exists(destination):
                destination = os.path.join(destination_folder, f"{name}_{i}{ext}")
                i += 1

        shutil.copy2(source, destination)
        print("File Copied =", file)
        count += 1

print("Total files copied =", count)
