from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q=deque()
    if cacheSize==0:
        return 5*len(cities)
    for city in cities:
        city=city.lower()
        if city in q:  
            answer+=1
            q.remove(city)  
            q.append(city)
        else:
            if len(q)<cacheSize:
                q.append(city)
            else:
                q.popleft()
                q.append(city)
            answer+=5
    return answer
