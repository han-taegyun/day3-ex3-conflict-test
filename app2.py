for n in range(100, 0, -1):
    claps = '짝' * str(n).count('3')
    print(claps if claps else n)