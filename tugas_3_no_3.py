n = 6 
for i in range(1, n+1):
    print('  ' * (n - i), end='')
    for j in range(1, i+1):
        if j == 1:
            print("*", end='')
        else:
            print(" . *", end='')
    print()
