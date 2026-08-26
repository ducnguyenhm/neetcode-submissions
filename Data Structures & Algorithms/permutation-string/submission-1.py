class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = {}
        for s in s1:
            cnt[s] = cnt.get(s, 0) + 1
        left = 0
        for right, s in enumerate(s2):
            if s in s1:
                cnt[s] = cnt.get(s, 0) - 1
            if s in s1 and cnt[s] == 0:
                del cnt[s]   
            if right - left + 1 == len(s1):
                print(cnt)
                if len(cnt) == 0:
                    return True
                if s2[left] in s1:
                    cnt[s2[left]] = cnt.get(s2[left], 0) + 1
                    if cnt[s2[left]] == 0:
                        del cnt[s2[left]]  
                left += 1          
        return False