def solution(priorities, location):
    answer = 0
    que=[]
    queIndex=[i for i in range(len(priorities))]
    while len(priorities)!=1:
        temp=priorities.pop(0)
        tempNum=queIndex.pop(0)
        if temp<max(priorities):
            priorities.append(temp)
            queIndex.append(tempNum)
        else:
            que.append(tempNum)
    que.append(queIndex.pop(0))
    return que.index(location)+1