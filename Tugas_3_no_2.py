def print_pattern(n):
    for i in range(n):
        print(" " * (i * 2) + "* " * (n - i))

n = 8
print_pattern(n)
