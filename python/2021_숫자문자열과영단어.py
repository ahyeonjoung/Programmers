def solution(s):
    answer = ''
    alpha=['zero','one','two','three','four','five','six','seven','eight','nine']
    temp=''
    for i in s:
        if '0'<=i<='9':
            temp=''
            answer+=i
        elif temp+i in alpha:
            answer+=str(alpha.index(temp+i))
            temp=''
        else:
            temp+=i
            
    return int(answer)