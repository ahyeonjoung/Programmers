import heapq 
from collections import defaultdict

def solution(n, s, a, b, fares):
    dis=defaultdict(list)
    result=[0 for i in range(n)]
    #딕셔너리 초기화
    for a1,b1,c1 in fares:
        dis[str(a1)].append([str(b1),c1])
        dis[str(b1)].append([str(a1),c1])
    #다익스트라 적용
    for i in range(1,n+1):
        result[i-1]=(dijkstra(dis,str(i)))

    #최소값 
    minNum=float('inf')
    for key in result[s-1]:
        num=result[s-1][key]+result[int(key)-1][str(a)]+result[int(key)-1][str(b)]
        if minNum>=num:
            minNum=num
    return minNum

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  #무한대로 초기화 
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  

    while queue:  
        current_distance, current_destination = heapq.heappop(queue)  

        if distances[current_destination] < current_distance:  
            continue
    
        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance  
            if distance < distances[new_destination]: 
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  
    
    return distances