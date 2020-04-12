# Programmers Algorithm 
# Heap Sort => More Hot

import heapq as hq

def solution(scoville, k):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= k:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1

    return answer

