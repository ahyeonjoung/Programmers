from collections import deque
def solution(record):
    answer=[]
    result=deque()
    dic={}
    for s in record:
        command=s.split()
        if command[0]!='Leave':

            dic[command[1]]=command[2]
        if command[0]=='Enter':
            result.append((command[1],'님이 들어왔습니다.'))
        elif command[0]=='Leave':
            result.append((command[1],'님이 나갔습니다.'))
            
    while result:
        Id,Co=result.popleft()
        answer.append(dic[Id]+Co)
      

    
    return answer