def solution(str_list):
    for c in str_list:
        if c == 'l':
            return str_list[:str_list.index(c)]
        elif c == 'r':
            return str_list[str_list.index(c)+1:]
        else:
            continue
    return []