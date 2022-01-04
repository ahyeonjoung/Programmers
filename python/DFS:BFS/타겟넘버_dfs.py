


def solution(numbers, target):
    result_list = [0]

    # i는 numbers의 각 원소들
    for i in range(len(numbers)):
        temp_list = []

        # result_list는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        for j in range(len(result_list)):
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        result_list = temp_list
        print(result_list)

    return result_list.count(target)
    

