import math
def solution(progresses, speeds):
    answer = []
    end=[] #걸리는날짜
    num=1 #날짜
    t=0 #비교대상
    for i in range(len(progresses)): #task당 걸리는날짜계산
        end.append(math.ceil((100-progresses[i])/speeds[i])) 
    for i in range(len(end)-1): #배포당 task개수 계산
        if end[i-t]<end[i+1]:
            answer.append(num)
            num=1
            t=0
        else:
            num+=1
            t+=1
    answer.append(num)
    return answer