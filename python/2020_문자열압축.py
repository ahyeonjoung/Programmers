import math
def solution(s):
    end=len(s)//2 #길이 반  
    maxNum=1000
    for i in range(1,end+1):
        temp=''
        numArr=[]
        flag=False
        num=1
        for j in range(math.ceil(len(s)/i)):
            a1=s[i*j:i*j+i]
            a2=s[i*j+i:i*j+i+i]
            if a1==a2 and flag: #처음이 아닌 반복문자 
                num+=1
                continue
            elif a1==a2 and not flag: #첫 반복문자 
                temp+=str(num)
                flag=True
            else: #반복문자 탈출 
                temp+=a1
                if num>=99: #반복되는 숫자가 100이상
                    numArr.append(2)
                elif num>=9: #반복되는 숫자가 10이상
                    numArr.append(1)
                num=1
                flag=False
        if len(temp)+sum(numArr)<maxNum: #최소값 업데이트
            maxNum=len(temp)+sum(numArr)
    
    if maxNum==1000: #문지열의 길이가 1일경우
        maxNum=1
        
    return maxNum 
