def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


def main():
    my_list = append_to('Python')
    print(my_list)

    my_longer_list = append_to('Is better than JavaScript')
    print(my_longer_list)


if __name__ == "__main__":
    main()
