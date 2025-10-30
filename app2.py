for i in range(100, 0, -1):
    count = str(i).count('3')
    if count > 0:
        print("짝" * count)
    else:
        print(i)
        