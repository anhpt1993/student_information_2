def input_text(text):
    return input(text)

def input_number(text, min, max):
    while True:
        try:
            grade = int(input(text))
            if min <= grade <= max:
                return grade
                break
            else:
                print("\nInvalid Value. Try again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try again!!!\n")

def choose_gender():
    gender = input_number("""
+) Gender:
    Choose one of the followings:
    1. Male
    2. Female
    3. Fluid

    Your choice: """, 1, 3)

    if gender == 1:
        return "Male"
    elif gender == 2:
        return "Female"
    else:
        return "Fluid"

def add_information():
    individual = []
    questions = [
        "+) Full name: ",
        "+) Gender: ",
        "+) Address: ",
        "+) Theory: ",
        "+) Practice: "
    ]

    for i in range(len(questions)):
        if i == 1:
            individual.append(choose_gender())
        elif i <= 2:
            individual.append(input_text(questions[i]))
        else:
            individual.append(input_number(questions[i], 0, 100))

    return individual

if __name__ == '__main__':
    sis = []
    for i in range(2):
        sis.append(add_information())
    print(sis)