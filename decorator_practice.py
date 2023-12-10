# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice
#
#
# @do_twice
# def greet_with_cake(name):
#     print(f"Cake for {name}!")
#
#
# greet_with_cake("everyone")


# def do_twice_with_list_args(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args[0], **kwargs)
#         func(*args[1], **kwargs)
#
#     return wrapper_do_twice
#
#
# @do_twice_with_list_args
# def greet_with_cake(name):
#     print(f"Cake for {name}!")
#
#
# greet_with_cake(args=["Chris", "Nabil"])


def do_twice(func):
    def wrapper_do_twice(*args):
        first_args = args[0] if len(args) > 0 else ""
        second_args = args[1] if len(args) > 1 else ""

        func(first_args)
        func(second_args)

    return wrapper_do_twice


@do_twice
def greet_with_cake(name):
    print(f"Cake for {name}!")


greet_with_cake("Chris", "Nabil")

