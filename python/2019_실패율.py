def solution(N, stages):
    answer = []
    trying=[0 for i in range(N)]
    correct=[0 for i in range(N)]
    ratio={}
    for i in stages:
        if i!=N+1:
            for r in range(i-1):
                trying[r]+=1
                correct[r]+=1
            trying[i-1]+=1
        else:
            for r in range(i-1):
                trying[r]+=1
                correct[r]+=1
    for i in range(N):
        if trying[i]!=0:
            ratio[i]=(trying[i]-correct[i])/trying[i]
        else:
            ratio[i]=0
            
    ratio=dict(sorted(ratio.items(), key = lambda item: item[1],reverse=True))
    
    for key in ratio:
        answer.append(key+1)
        
    return answer
