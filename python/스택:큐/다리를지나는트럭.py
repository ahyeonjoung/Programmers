def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length #빈도로
    while len(trucks_on_bridge):
        answer += 1 #초 증가
        trucks_on_bridge.pop(0) #앞차량삭제
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0)) #새로운차량추가
            else:
                trucks_on_bridge.append(0) #기존차량만 앞으로
    return answer