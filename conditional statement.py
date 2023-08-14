def conditional_statement(number):
    if 80 <= number <= 100:
        print("A+")

    elif number >= 75:
        print("A")

    elif number >= 70:
        print("A-")

    elif number >= 65:
        print("B+")

    elif number >= 60:
        print("B")

    elif number >= 55:
        print("B-")

    elif number >= 50:
        print("C+")

    elif number >= 45:
        print("C")

    elif number >= 40:
        print("D")

    elif 0 <= number < 40:
        print("Fail")

    else:
        print("Invalid Input")


conditional_statement(16)
