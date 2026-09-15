c, n = 0, 1

while c < 4:
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        t=1
        for i in range(1, n):
            if n % i == 0:
                if t:
                    print(i, end="")
                    t = 0
                else:
                    print(" +", i, end="")
        print(" =", n)
        c += 1
    n += 1
while 1:
    try:
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        if sum == n:
            t = 1

            for i in range(1, n):
                if n % i == 0:
                    if t:
                        print(i, end="")
                        t = 0
                    else:
                        print(" +", i, end="")
            print(" =", n, "is a perfect number.")
        else:
            print(n, "is not a perfect number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")