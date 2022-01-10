# Runtime: 44 ms, faster than 84.05% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 44.81% of Python online submissions for Longest Substring Without Repeating Characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ##MOST OPTIMIZED VERSION - OPTIMIZED SLIDING WINDOW PANE METHOD
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
