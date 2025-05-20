for tc in range(1, 11):
    dump = int(input())

    boxes = list(map(int, input().split()))

    while dump > 0:
        if max(boxes) - min(boxes) < 2:
            dump = 0
        else:
            boxes[boxes.index(max(boxes))] -= 1
            boxes[boxes.index(min(boxes))] += 1
            dump -= 1

    print(f'#{tc} ', end='')
    print(max(boxes) - min(boxes))