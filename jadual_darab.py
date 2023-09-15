def jadualDarab():
    for x in range(46):
        print("*", end="")
    print()

    print("\t\t\t\tJADUAL DARAB")

    for x in range(46):
        print("*", end="")
    print()

    start = 1
    end = 12

    for i in range(start, end + 1):
        for j in range(start, end + 1):
            product = i * j
            print(f"{product}", end="\t")
        print()

if __name__ == '__main__':
    jadualDarab()
