def solution(begin, target, words):
    arr=[]
    num=0
    if target not in words:
        return 0
    DFS(begin,target,words,0,[],arr)
    if len(arr)==0:
        return 0
    else:
        return min(arr)

def DFS(begin, target, words,num,log,arr):
    if begin==target:
        arr.append(num)
    else:
        co=[]
        for word in words:
            if word not in log:
                temp=0
                for i in range(len(word)):
                    if word[i]==begin[i]:
                        temp+=1
                if temp== len(word)-1:
                    co.append(word)
        for word in co:           
            log.append(word)
            DFS(word,target,words,num+1,log,arr)