class Solution(object):
    def topKFrequent(self, nums, k):
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        heap = []
        answer = []
        elements = len(countMap)
        for key in countMap:
            heappush(heap, tuple([-countMap[key], key]))
            if len(heap) > elements - k:
                answer.append(heappop(heap)[1])
        
        return answer