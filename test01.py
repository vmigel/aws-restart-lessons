x = 10  # x is a global variable

def outer_function():
    # Enclosing namespace
    y = 20  # y is a nonlocal variable

    def inner_function():
        # Local namespace
        z = 30  # z is a local variable
        print("Inside inner_function:")
        print("z =", z)
        print("y =", y)
        print("x =", x)

    inner_function()

outer_function()

print("Outside functions:")
print("x =", x)
print("z =", z)
print("y =", y)