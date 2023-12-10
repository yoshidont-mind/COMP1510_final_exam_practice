global_variable = 'global_variable'


def outer(outer_parameter='outer_parameter'):
    local_variable_in_outer = 'local_variable_in_outer'
    global_variable = 'GLOBAL_VARIABLE'

    def inner():
        print(global_variable, outer_parameter, local_variable_in_outer)

    return inner()


def main():
    function_to_execute = outer()
    function_to_execute()
    print(global_variable)


if __name__ == "__main__":
    main()
