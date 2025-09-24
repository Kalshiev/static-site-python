import os
import shutil

def delete_dir(dir):
    if os.path.exists(dir):
        files = os.listdir(dir)
        for file in files:
            print(f"deleting... {file}")
        shutil.rmtree(dir)
    os.mkdir(dir)

def copy_dir(source, destination):
    source_dir = os.path.abspath(source)
    destination_dir = os.path.abspath(destination)
    
    if os.path.exists(source_dir):
        files = os.listdir(source_dir)
        for file in files:
            file_path = os.path.join(source_dir, file)
            if os.path.isfile(file_path):
                print(f"copying... {file_path}")
                shutil.copy(file_path, destination_dir)
            elif os.path.isdir(file_path):
                new_destination = os.path.join(destination_dir, file)
                os.mkdir(new_destination)
                copy_dir(file_path, new_destination)

delete_dir("./public")
copy_dir("./static", "./public")