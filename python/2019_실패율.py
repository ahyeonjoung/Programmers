def solution(N, stages):
    answer = []
    trying=len(stages)
    correct=0
    for x in range(1,N+1):
        for y in stages:
            if x==y:
                correct+=1
        if correct>0:
            answer.append(correct/trying)
            trying-=correct
            correct=0
        else:
            answer.append(0)
    answer=sorted(range(len(answer)),key=lambda k: answer[k],reverse=True)
    answer=[x+1 for x in answer]
    return answer
                
    