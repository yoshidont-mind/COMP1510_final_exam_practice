# Let's execute the code from the third image and calculate the sum of the integers in the final row.

def print_something(size):
    numbers = list(range(1, size + 1))

    for number in numbers:
        print('\t' + str(number), end='')
        pass

    for number in numbers:
        print(number, end='')
        for other_number in numbers:
            print('\t' + str(number * other_number), end='')
        print()


def main():
    print_something(4)


if __name__ == "__main__":
    main()
