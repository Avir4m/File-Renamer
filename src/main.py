import shutil, os
 
folder = "Files"
renamed_folder = "Renamed_Files"

for count, filename in enumerate(os.listdir(folder)):
    test, file_extention = os.path.splitext((filename))
    new_name = f"{str(count)}{file_extention}"
    src =f"{folder}/{filename}"
    dst =f"{renamed_folder}/{new_name}"
    shutil.copy(src, dst)
    print("Rename", {src}, "to", {dst})

print("Success!")