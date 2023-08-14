def continue_statement(num):
    for i in range(1, 10, 2):
        if i == num:
            continue
        print(i)


continue_statement(5)

print("\n")


def break_statement(num):
    for i in range(1,10):
        if i == num:
            break
        print(i)


break_statement(6)
