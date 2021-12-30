import itertools

def solution(numbers):
    answer = 0
    numbers=list(numbers) #문자열 분리
    numArray=[]
    result=[]
    for i in range(len(numbers)):
        result.append(list(itertools.permutations(numbers,i+1)))
        numArray.append([int(("").join(p)) for p in result[i]])
    num= set(sum(numArray, []))  #중복제거
    for i in num:
        if primeNumber(i):
            answer+=1
    return answer

def primeNumber(num): #소수판별함수
    if num==1 or num==0:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True