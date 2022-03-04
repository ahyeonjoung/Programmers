import heapq
from collections import defaultdict
def dijkstra(graph,start):
    distances={node: float('inf') for node in graph}
    distances[start]=0
    queue=[]
    heapq.heappush(queue,[distances[start],start]) 
    while queue:
        current_distance, current_destination=heapq.heappop(queue)
        if distances[current_destination]<current_distance:   
            continue
        for new_destination, new_distance in graph[current_destination]:
            distance=current_distance+new_distance
            if distance<distances[new_destination]:
                distances[new_destination]=distance
                heapq.heappush(queue,[distance,new_destination])
    return distances

def solution(N, road, K):
    answer = 0
    result=[]
    board=defaultdict(list)
    for a,b,c in road:
        board[str(a)].append([str(b),c])
        board[str(b)].append([str(a),c])
    result=dijkstra(board,'1')

    for i in result.values():
        if i<=K:
            answer+=1




    return answer
