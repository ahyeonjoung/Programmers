from collections import defaultdict
from copy import deepcopy
max_sheep = 0

def solution(info, edges):
    answer = 0
    node=defaultdict(list)
    for a,b in edges:
        node[a].append(b)
    visited=[False]*(len(edges)+1)
    dfs(0,visited,info,0,0,node,[])

    return max_sheep

def dfs(start,visited,info,sheep,wolf,node,candi):
    global max_sheep
    if visited[start]:
        return 
    visited[start]=True
    if info[start]==0:
        sheep+=1
        max_sheep=max(max_sheep,sheep)
    else:
        wolf+=1
    if sheep<=wolf:
        return

    candi+=node[start]
    for i in candi:
        dfs(i,deepcopy(visited),info,sheep,wolf,node,candi=[loc for loc in candi if loc != i and not visited[loc]])