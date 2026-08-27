class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current_window = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in current_window:
                current_window.remove(s[left])
                left += 1

            current_window.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length