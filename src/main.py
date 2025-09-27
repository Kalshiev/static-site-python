from copy_all_files import *
from generate_page import generate_page_recursive
import sys

basepath = sys.argv[1]
def main():
    delete_dir("docs")
    copy_dir("./static", "docs")
    generate_page_recursive("./content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()