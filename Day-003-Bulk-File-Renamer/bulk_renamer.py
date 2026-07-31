import os 

folder = "images"

for count, filename in enumerate(os.listdir(folder), start=1):
    extension = os.path.splitext(filename)[1]

    new_name = f"image_{count}{extension}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

    print(f"{filename} -> {new_name}")

print("Renaming completed.")