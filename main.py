def DecreaseElements():
    vals = [[96, 5, 23, 16, 45, 63], [20, 106, 50, 27, 38, 15]]


    for i in range(len(vals)):
        for j in range(len(vals[i])):
            vals[i][j] -= 1

    for i in range(len(vals)):
        for j in range(len(vals[i])):
            print(vals[i][j], end=" ")
        print()

        # testing
DecreaseElements()
