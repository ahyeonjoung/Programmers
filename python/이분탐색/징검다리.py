def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    
    left,right=0,distance
    while left<=right:
        mid=(left+right)//2
        min_distance=float('inf')
        current=0 #현재거리
        remove_cnt=0 #바위를 제거한 개수
        for rock in rocks:
            diff=rock-current
            if diff<mid:
                remove_cnt+=1
            else:
                current=rock #현재거리저장
                min_distance=min(min_distance,diff)
        if remove_cnt>n:
            right=mid-1
        else:
            answer=min_distance
            left=mid+1
       
                

    return answer