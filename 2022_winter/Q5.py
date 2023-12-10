try:
    value = float('abc123')
except Exception:
    print("That's not going to work!")
except ValueError:
    print("Wrong value, that's not a float!")
except TypeError:
    print("Wrong type, I can't convert that!")