import os
import shutil

# get the path from this folder
this_folder = os.path.abspath(os.getcwd())

# create a list with filenames from txt file
with open("files_list.txt") as f:
    list_files = f.read().splitlines() 

# set the origin and destiny folder
origin = f"{this_folder}/origin/"
destiny = f"{this_folder}/destiny/"

# get all filenames in the origin path
all_filenames_in_path = [file for file in os.listdir(origin)]

# move only files don't typed on files_list.txt
for file in all_filenames_in_path:
    if file not in list_files:
        origin = f"{this_folder}/origin/{file}"
        shutil.move(origin, destiny)