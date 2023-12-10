import math


def square_list_with_for_loop(numbers):
    list_to_return = []
    for number in numbers:
        list_to_return.append(number ** 2)
    return list_to_return


def square_list_with_list_comprehension(numbers):
    return [number ** 2 for number in numbers]


def square_list_with_map(numbers):
    return list(map(lambda number: number ** 2, numbers))


def square_odd_numbers_with_filter_and_map(numbers):
    return list(map(lambda number: number ** 2, filter(lambda number: number % 2 == 1, numbers)))


def square_odd_numbers_with_list_comprehension(numbers):
    return [number ** 2 for number in numbers if number % 2 == 1]


def factorial_list_with_map(numbers):
    return list(map(lambda number: math.factorial(number), numbers))


def factorial_list_with_list_comprehension(numbers):
    return [math.factorial(number) for number in numbers]


def factorial_prime_numbers_with_map_and_filter(numbers):
    return list(map(lambda number: number ** 2, filter(lambda number: is_prime(number), numbers)))


def is_prime(number):
    if number % 2 == 0:
        return False

    sqrt_number = int(math.floor(math.sqrt(number)))
    for divisor in range(3, sqrt_number + 1, 2):
        if number % divisor == 0:
            return False
    return True


def factorial_prime_numbers_with_list_comprehension(numbers):
    return [number ** 2 for number in numbers if is_prime(number)]


def add_lists_together(list_first, list_second):
    """

    :param list_first:
    :param list_second:
    :return:
    >>> test_list_first = [1, 2, 3]
    >>> test_list_second = [4, 5, 6]
    >>> add_lists_together(test_list_first, test_list_second)
    [5, 7, 9]
    >>> test_list_first = [1]
    >>> test_list_second = [0]
    >>> add_lists_together(test_list_first, test_list_second)
    [1]
    """
    return list(map(lambda number_first, number_second: number_first + number_second, list_first, list_second))


def string_to_ord_list(string):
    """

    :param string:
    :return:
    >>> test_string = "python"
    >>> string_to_ord_list(test_string)
    [112, 121, 116, 104, 111, 110]
    >>> test_string = "a"
    >>> string_to_ord_list(test_string)
    [97]
    """
    return list(map(lambda letter: ord(letter), string))


def combined_length(list_first, list_second, list_third):
    """

    :param list_first:
    :param list_second:
    :param list_third:
    :return:
    >>> test_list_first = ["hello", "world"]
    >>> test_list_second = ["python", "a"]
    >>> test_list_third = ["yamada", "b"]
    >>> combined_length(test_list_first, test_list_second, test_list_third)
    [17, 7]
    """
    return list(map(lambda string_first, string_second, string_third: len(string_first) + len(string_second) + len(
        string_third), list_first, list_second, list_third))


def main():
    # 1 (a) ~ (f)
    data = list(range(1, 11))
    function_list = [square_list_with_for_loop, square_list_with_list_comprehension, square_list_with_map,
                     square_odd_numbers_with_filter_and_map, square_odd_numbers_with_list_comprehension,
                     factorial_list_with_map, factorial_list_with_list_comprehension]
    for function in function_list:
        print(f"{function.__name__}(): {function(data)}")
    print()

    # 2 (a) ~ (c)
    data_second = list(range(1, 12))
    function_list = [factorial_prime_numbers_with_map_and_filter, factorial_prime_numbers_with_list_comprehension]
    for function in function_list:
        print(f"{function.__name__}(): {function(data_second)}")


if __name__ == "__main__":
    main()
