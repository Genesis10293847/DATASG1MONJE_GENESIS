while 1:
    try:
        c = input("Enter what you want to solve (d/v/t): ").lower()

        if c == "d":
            v = float(input("Enter velocity: "))
            t = float(input("Enter time: "))
            d = v * t
            print("Distance =", d)

        elif c == "v":
            d = float(input("Enter distance: "))
            t = float(input("Enter time: "))

            if t == 0:
                print("Time cannot be 0.")
                continue

            v = d / t
            print("Velocity =", v)

        elif c == "t":
            d = float(input("Enter distance: "))
            v = float(input("Enter velocity: "))

            if v == 0:
                print("Velocity cannot be 0.")
                continue

            t = d / v
            print("Time =", t)

        else:
            print("Please enter d, v, or t.")

    except ValueError:
        print("Invalid input. Please enter a number.")