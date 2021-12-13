import math
def solution(clothes):
    answer = 1
    cloth={}
    for i in range(len(clothes)):
        if clothes[i][1] in cloth:
            cloth[clothes[i][1]]+=1
        else:
            cloth[clothes[i][1]]=1
    
    num=list(cloth.values())
    for i in num:
        answer*=i+1
    return answer-1