from copy_all_files import *

def main():
    delete_dir("./public")
    copy_dir("./static", "./public")


if __name__ == "__main__":
    main()