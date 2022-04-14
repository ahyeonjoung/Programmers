from collections import Counter
def solution(str1, str2):
    cr,al = 0,0
    str1=str1.lower()
    str2=str2.lower()
    a=[]
    b=[]

    for i in range(len(str1)-1):
        if 'a'<=str1[i]<='z' and 'a'<=str1[i+1]<='z':
            a.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if 'a'<=str2[i]<='z' and 'a'<=str2[i+1]<='z':
            b.append(str2[i]+str2[i+1])

    if not a and not b:
        return 65536

    a=Counter(a)
    b=Counter(b)
    
    for temp in a:
        if temp in b:
            cr+=min(a[temp],b[temp])
            al+=max(a[temp],b[temp])
            b.pop(temp)
        else:
            al+=a[temp]
    al+=sum(b.values())
    return int(cr/al*65536)
