def solution(routes):
    answer = 1
    routes.sort()
    camera=[routes[0][0],routes[0][1]] #카메라 초기상태
    routes.pop(0)
    for arr in routes:
        if arr[0]>camera[1]: #범위초과
            answer+=1
            camera=[arr[0],arr[1]]
        else: #범위수정
            if camera[1]<arr[1]:
                camera[0]=arr[0]
            else:
                camera[1]=arr[1]
    return answer