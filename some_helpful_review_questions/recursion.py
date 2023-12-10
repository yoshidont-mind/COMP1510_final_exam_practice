# Q6
def sum_of_evens(number):
    if number < 2:
        return 0
    else:
        return (number // 2) * 2 + sum_of_evens(number - 2)


def main():
    print(sum_of_evens(9))


if __name__ == "__main__":
    main()
