# def my_decorator(func):
#     def wraperr_func():
#         print("***")
#
#         func()
#
#         print("***")
#     return wraperr_func()
#
# @my_decorator
# def hello():
#     print("numbers")
#
# @my_decorator
# def fuck():
#     print('fuck you')
#
# hello
# fuck

#how decorators work behind the scene or its a magic???
def my_decorator(func):
    def wraperr_func():
        print("***")

        func()

        print("***")
    return wraperr_func()

def hello():
    print("numbers")


def fuck():
    print('fuck you')

a = my_decorator(hello)
a
my_decorator(fuck)

