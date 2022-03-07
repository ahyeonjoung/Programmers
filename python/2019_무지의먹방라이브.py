import heapq
def solution(food_times, k):
    answer = -1 
    h = [] 
    for i in range(len(food_times)): 
        heapq.heappush(h, (food_times[i], i + 1)) 
    length = len(food_times)  
    zero = 0 
    while h:
        time=(h[0][0]-zero)*length
        if k>=time:
            k-=time
            zero,_=heapq.heappop(h)
            length-=1
        else:
            idx=k%length
            h.sort(key=lambda x: x[1]) 
            answer=h[idx][1]
            break
    return answer