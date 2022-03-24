def manhaton(r1,c1,r2,c2):
    distance=abs(r1-r2)+abs(c1-c2)
    return distance
    
def solution(places):
    answer = []
    for place in places:
        human=[]
        flag=True
        for i in  range(5):
            for j in range(5):
                if place[i][j]=='P':
                    human.append([i,j])
        for i in range(len(human)):
            for j in range(i+1,len(human)):
                r1,c1=human[i]
                r2,c2=human[j]
                if manhaton(r1,c1,r2,c2)<=1:
                    flag=False
                    break
                elif manhaton(r1,c1,r2,c2)==2:
                    if r1==r2:
                        if place[r1][(c1+c2)//2]!='X':
                            flag=False
                            break
                    elif c1==c2:
                        if place[((r1+r2)//2)][c1]!='X':
                            flag=False
                            break
                    else:
                        if place[r1][c2]!='X' or place[r2][c1]!='X':
                            flag=False
                            break
            if not flag:
                answer.append(0)
                break

        else:
            answer.append(1)

    return answer
