def main():
    days = ['Mon', 'Yes', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    weekend = enumerate(days)[5:]
    for day in weekend:
        print(day[0], day[1])


if __name__ == "__main__":
    main()
