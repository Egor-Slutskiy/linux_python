input_msg = input("Input two numeral: ")
x, y = input_msg.split(" ")
x = int(x)
y = int(y)


def some_calculations(x, y):
    return x + y


print(some_calculations(x, y))
