from module_add import *
from module_delete import *
def choose_option():
    while True:
        try:
            option = int(input("""
            Choose one of the following options to execute program
            1. Display all list
            2. Add
            3. Delete
            4. Exit
            
            Your choice: """))
            if 1 <= option <= 4:
                return option
                break
            else:
                print("\nInvalid Input. Try again!!!\n")
        except ValueError:
            print("\nInvalid Input. Try again!!!\n")
    

def display_information(*list):
    info = "{:^5}|{:^20}|{:^10}|{:^20}|{:^10}|{:^10}"
    print(info.format("S/N", "FULL NAME", "GENDER", "CITY", "THEORY", "PRACTICE"))

    for i in range(len(list)):
        print(info.format(i + 1, list[i][0], list[i][1], list[i][2], list[i][3], list[i][4]))

def try_again(text):
    answer = input(text).upper().strip()
    if answer == "Y" or answer == "YES":
        return True
    else:
        return False

if __name__ == '__main__':
    sis = []
    while True:
        option = choose_option()
        if option == 1:
            if sis == []:
                print("\nYou have to add student information first!!!\n".upper())
            else:
                display_information(*sis)
        elif option == 2:
            choice = True
            while choice:
                sis.append(add_information())
                choice = try_again("\nYou you want to add more students? (Y/N): ")
        elif option == 3:
            if sis == []:
                print("\nNothing to delete. You have to add information first\n".upper())
            else:
                choice = True
                while choice:
                    item = choose_item(*sis)
                    sis = remove_item(item, *sis)
                    choice = try_again("\nYou you want to delete more? (Y/N): ")
        else:
            exit()