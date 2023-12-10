def follows(first, second):
    return not first or second


def main():
    high_temperatures = True
    melting_arctic_ice = True
    rising_sea_levels = True  # Sea levels are rising
    smoky_summers = False  # All regions become hot
    climate_change = follows(follows(high_temperatures, melting_arctic_ice), rising_sea_levels)

    if not smoky_summers:
        print(climate_change)
    else:
        print(smoky_summers)


if __name__ == "__main__":
    main()
