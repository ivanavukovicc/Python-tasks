def move_zeros_to_end(num):

    non_zero = 0

    for i in range(len(num)):
        if num[i] != 0:
            num[non_zero], num[i] = num [i], num[non_zero]
            non_zero += 1

    return num


# Prethodno resenje koristilo je 'remove' metod koji je svaki put trazio
# i uklanjao prvo pojavljivanje nule. Zbog toga je imalo dosta ponavljanja
