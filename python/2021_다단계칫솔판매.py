from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    rec=defaultdict(list)
    enr={}
    i=0
    for a,b in zip(enroll,referral):
        rec[a]=b
        enr[a]=i
        i+=1

    
    for name,price in zip(seller,amount):
        dfs(name,price*100,rec,answer,enr)
    return answer

def dfs(name,amount,rec,answer,enroll):
    your=int(amount*0.1)
    answer[enroll[name]]+=amount-your
    if your<1:
        return answer
    if rec[name]=='-':
        return answer
    dfs(rec[name],your,rec,answer,enroll)
