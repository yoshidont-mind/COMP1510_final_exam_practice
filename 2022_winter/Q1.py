# Let's execute the code from the first image and observe the output to answer the question.
def make_priority_queue():
    queue = []

    def enqueue(new_value, pop):
        queue.append(new_value)
        queue.sort()
        if pop:
            return queue.pop(0)
        else:
            return queue[0]
    return enqueue


def main():
    test_queue = make_priority_queue()
    print(test_queue("Juan", False))
    print(test_queue("Jack", True))
    print(test_queue("Joe", True))
    print(test_queue("Jesper", False))
    print(test_queue("Jerry", True))
    print(test_queue("Josh", True))


if __name__ == "__main__":
    main()
