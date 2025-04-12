def solution(my_string, queries):
#     mstr = my_string
#     for s, e in queries:
#         answer = ''
#         buffer = ''
        
#         for i in range(0,s):
#             answer += mstr[i]
#         for i in range(s, e+1):
#             buffer += mstr[i]
#         answer += ''.join(reversed(buffer))
#         for i in range(e+1, len(my_string)):
#             answer += mstr[i]
            
#         mstr = answer
#     return answer    
        
    # 쓸데없이 개어렵게 풀었네
    
    answer = list(my_string)
    for s, e in queries:
        answer[s:e+1] = answer[s:e+1][::-1]
    return ''.join(answer)
            
    