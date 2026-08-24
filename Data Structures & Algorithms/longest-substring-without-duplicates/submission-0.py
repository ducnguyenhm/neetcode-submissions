class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        include = set()
        while right < len(s):
            if s[right] in include:
                while left < right:
                    include.remove(s[left])
                    if s[left] == s[right]:
                        left += 1
                        break
                    left += 1
            include.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest
