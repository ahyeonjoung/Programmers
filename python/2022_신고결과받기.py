def solution(id_list, report, k):
    answer = [0]*len(id_list)
    countArr=[0]*len(id_list)
    name={}
    report=set(report)
    for id in id_list:
        name[id]=[]
    for a in report:
        h1,h2=a.split()
        findIndex=id_list.index(h2)
        countArr[findIndex]+=1
        name[h2].append(h1)
    
    for i in range(len(countArr)):
        if countArr[i]>=k:
            for t in name[id_list[i]]:
                answer[id_list.index(t)]+=1
                       
    return answer