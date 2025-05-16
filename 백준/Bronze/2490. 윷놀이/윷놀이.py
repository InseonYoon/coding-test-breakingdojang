for _ in range(3):
    yut = sum(list(map(int, input().split())))
    if yut == 3:
        print('A')
    elif yut == 2:
        print('B')
    elif yut == 1:
        print('C')
    elif yut == 0:
        print('D')
    else:
        print('E')