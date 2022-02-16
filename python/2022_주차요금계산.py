from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    car=defaultdict(list) 
    temp=[]
    for record in records:
        time,number,IO=record.split()
        car[number].append(time)
    for i in car:
        if len(car[i])%2!=0:
            car[i].append('23:59')
    for time in car:
        sumTime=0
        for t in range(0,len(car[time]),2):
            h1,m1=car[time][t].split(':')
            h2,m2=car[time][t+1].split(':')
            sumTime+=time_cal(h1,m1,h2,m2)
        
        temp.append([time,sumTime])
    temp.sort()
    for a in temp:
        if a[1]<=fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((a[1]-fees[0])/fees[2])*fees[3])
    return answer


def time_cal(h1,m1,h2,m2):
    h1,m1,h2,m2=int(h1),int(m1),int(h2),int(m2)
    return (h2*60+m2)-(h1*60+m1)