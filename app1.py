for num in range(1, 101):    
    if num % 2 == 0 or num % 5 == 0:
        print(f"{num}은 2 또는 5의 배수입니다.")
    else:
        print(num)
