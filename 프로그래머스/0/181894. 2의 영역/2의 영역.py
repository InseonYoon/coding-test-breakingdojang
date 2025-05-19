def solution(arr):
    idx = [i for i, val in enumerate(arr) if val == 2]
    if len(idx) > 1:
        return arr[idx[0]:idx[-1]+1]
    elif len(idx) == 1:
        return [arr[idx[0]]]
    else:
        return [-1]