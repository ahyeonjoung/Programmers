def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:(x[2],x[0]))
    bridge=set([costs[0][0]])
    #kruscal 알고리즘
    while len(bridge)!=n:
        for i, num in enumerate(costs):
            if num[0] in bridge and num[1] in bridge:
                continue
            if num[0] in bridge or num[1] in bridge:
                bridge.update([num[0],num[1]])
                answer+=num[2]
                costs[i]=[-1,-1,-1]
                break
            
    return answer


    