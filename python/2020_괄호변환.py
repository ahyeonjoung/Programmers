from collections import deque
def solution(p):
    answer = ''
    if p=='':
        return ''
    u,v=divide(p)
    if correct(u):
        return u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        for c in u[1:len(u)-1]:
            if c=="(":
                answer+=")"
            else:
                answer+='('
        return answer


def divide(w):
    openNum=0
    closeNum=0
    for i in range(len(w)):
        if w[i]=="(":
            openNum+=1
        else:
            closeNum+=1
        if openNum==closeNum:
            u=w[:i+1]
            v=w[i+1:]
            return u,v

def correct(w):
    stack=[]
    for c in w:
        if c=='(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except:
                return False
    return True