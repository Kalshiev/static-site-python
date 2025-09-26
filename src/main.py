from copy_all_files import *
from generate_page import generate_page_recursive, generate_page

def main():
    delete_dir("./public")
    copy_dir("./static", "./public")
    generate_page_recursive("./content", "template.html", "public")


if __name__ == "__main__":
    main()