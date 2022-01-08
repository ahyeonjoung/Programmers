from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for n in course:
        candidates = []
        for order in orders:
            for li in combinations(order, n):
                temp = ''.join(sorted(li))
                candidates.append(temp)
        count= Counter(candidates).most_common() 
        answer += [menu for menu, cnt in count if cnt > 1 and cnt == count[0][1]]
    answer.sort()
            
    return answer