def solution(n, arr1, arr2):
    answer = []
    for key1, key2 in zip(arr1,arr2):
        temp=''
        key1=format(key1,'b').zfill(n)
        key2=format(key2,'b').zfill(n)
        for k1,k2 in zip(key1,key2):
            if k1=='1' or k2=='1':
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
    return answer
