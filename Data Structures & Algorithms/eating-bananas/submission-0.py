class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_finish(k):
            ans = 0
            for pile in piles:
                if pile % k == 0:
                    time = pile // k
                else:
                    time = pile // k + 1 
                ans += time              
            return ans

        
        start = 1
        end = max(piles)
        print(start, end)
        while start < end:
            mid = (start + end) // 2
            time_mid = is_finish(mid)
            if mid == 0 and time_mid <= h or time_mid <= h and is_finish(mid - 1) > h:
                return mid
            if time_mid <= h:
                end = mid - 1
            else:
                start = mid + 1
        
        if is_finish(start) > h:
            return -1
        return start

            