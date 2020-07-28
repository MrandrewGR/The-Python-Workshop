a, b = 24, 36
check = True

i = 1

while check:
    if i % a == 0 and i % b == 0:
        print(i)
        check = False
    i += 1

    #честно подсмотрел в решении