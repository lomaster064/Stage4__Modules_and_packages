def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    return inner_function

in_function = test_function()

print(in_function)

#inner_function() # NameError: name 'inner_function' is not defined.

# Эта функция вызывает inner_function
in_function()