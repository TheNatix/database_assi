from utils import create
from utils import after_create
from utils import menu
def main():
    create.creatingdb()
    after_create.importing()
    menu.main_menu()


if __name__ == "__main__":
    main()