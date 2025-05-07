def solution(my_string):
    answer = [0 for i in range(52)]
    test = ''
    for i in range(len(my_string)):
        index = ord(my_string[i])-(65 if (ord(my_string[i])<91) else 71) 
        answer[index] += 1
        test += my_string[i]+', '+str(ord(my_string[i])-65)+' / '
    return answer