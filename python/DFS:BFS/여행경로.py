import collections
answer = []
graph = collections.defaultdict(list)

def dfs(s):
    while graph[s]:
        print('graph',graph[s])
        dfs(graph[s].pop(0)) #단어순 첫번째단어만

    if s not in graph[s]: 
        answer.append(s) 
        return

def solution(tickets):
    
    for a,b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort()
       
    dfs("ICN")

    return answer[::-1] #거꾸로출력