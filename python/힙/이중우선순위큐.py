import heapq
def solution(operations):
    minHeap=[] #최소힙
    maxHeap=[] #최대힙
    for op in operations:
        temp=op.split(' ')
        if temp[0]=='I':
            heapq.heappush(minHeap, int(temp[1]))
            heapq.heappush(maxHeap, (-int(temp[1]), int(temp[1])))
        elif temp[0]=='D' and len(minHeap)>0:
            if temp[1]=='1':
                num=heapq.heappop(maxHeap)
                minHeap.remove(num[1])
            else:
                num=heapq.heappop(minHeap)
                maxHeap.remove((-num,num))

    if len(minHeap)==0:
        return [0,0]
    else:
        return [heapq.heappop(maxHeap)[1],heapq.heappop(minHeap)]