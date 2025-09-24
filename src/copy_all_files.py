import os
import shutil

def delete_dir(dir):
    if os.path.exists(dir):
        files = os.listdir(dir)
        for file in files:
            print(f"deleting... {file}")
        shutil.rmtree(dir)
    else:
        print("Directory already deleted!")
        print("Refreshing the directory")
        os.mkdir("public")

def copy_dir(source, destination):
    if os.path.exists(source):
        files = os.listdir(source)
        for file in files:
            s_path = os.path.abspath(file)
            print(s_path)


copy_dir("./static", "./public")