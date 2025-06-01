from collections import defaultdict

def solution(id_list, report, k):
    id_index = {user: i for i, user in enumerate(id_list)}
    answer = [0] * len(id_list)
    
    report = set(report)
    reported_by = defaultdict(set) #각 이용자를 신고한 이용자 목록
    
    for r in report:
        goodid, badid = r.split()
        reported_by[badid].add(goodid)
        
    for badid, reporters in reported_by.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_index[reporter]] +=1
            
    return answer