altura = 999

for i in range(altura):
    for k in range(2 * i + 1):
        print("*", end="")

    for j in range(altura - i - 1):
        print(" ", end="")
    

    print()