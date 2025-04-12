def solution(my_string):
    return my_string.translate({ord(l): None for l in 'aeiou'})