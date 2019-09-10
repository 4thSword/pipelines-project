#imports
from menus import *
#app
def main():
    args = get_args()
    main_menu(args.difficulty, args.gamestyle)
    
if __name__ == "__main__":
    main()