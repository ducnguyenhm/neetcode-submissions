class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1 2 1 => heap ((2, 1) (1, 0) (1, 1))  
        # 2 1 0 => remove => heap ((2, 1) (1, 0) (1, 1))
        # 1 0 4 => push heap => remove => heap ((4, 2), (0, 2))
        # remove => you remove all the element not in the sliding window

        curr = []
        ans = []
        heapq.heapify(curr) #O(k)
        for i in range(k):
            heapq.heappush(curr, [-nums[i], i])
        #print(curr)

        ans.append(-curr[0][0])
        right = k
        left = 0
        while right < len(nums):
            heapq.heappush(curr, [-nums[right], right])
            while curr[0][1] <= left:
                heapq.heappop(curr) 
            ans.append(-curr[0][0])
            left += 1
            right += 1
        return ans
