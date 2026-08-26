class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        ans = 0
        max_letter = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_letter = max(max_letter, count[s[right]])
            if (right - left + 1) - max_letter > k:
                count[s[left]] -= 1
                left += 1
            else:
                
                ans = max(right - left + 1, ans)
            print(count[s[right]])
            right += 1
        return ans