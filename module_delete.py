def remove_item(index, *array):
    temp_list = list(array).copy()
    temp_list.pop(index - 1)
    return temp_list

def choose_item(*array):
    while True:
        try:
            index = int(input("Enter S/N to delete: "))
            if 1 <= index <= len(array):
                return index
                break
            else:
                print("\nInvalid Value. Try Again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")

if __name__ == '__main__':
    array = [
        ["Pham The Anh", "Male", "Vung Tau", 75, 75],
        ["Le Thi Nga", "Female", "Vung Tau", 70, 80]
    ]
    item = choose_item(*array)
    array = remove_item(item, *array)
    print(array)