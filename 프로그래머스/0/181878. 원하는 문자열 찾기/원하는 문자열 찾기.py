def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    return 1 if myString.count(pat) > 0 else 0