"""
🔗 Problem: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

🧠 Level: Medium

🎯 Goal:
Given a string `s`, find the length of the longest substring without repeating characters.

🧪 Examples:
Input: s = "abcabcbb"   => Output: 3   (Substring: "abc")
Input: s = "bbbbb"      => Output: 1   (Substring: "b")
Input: s = "pwwkew"     => Output: 3   (Substring: "wke")
"""

# 🚀 Brute Force Approach
# ------------------------
# Try all substrings and check if they have duplicates.
# Time Complexity: O(n^3) – Generating all substrings and checking uniqueness
# Space Complexity: O(n) – For storing the substring
def length_of_longest_substring_bruteforce(s: str) -> int:
    def all_unique(sub: str) -> bool:
        return len(set(sub)) == len(sub)

    max_len = 0
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            if all_unique(s[i:j]):
                max_len = max(max_len, j - i)

    return max_len

# ⚡ Better Approach (Using HashSet)
# ----------------------------------
# Use a sliding window with two pointers and a set to track characters.
# Time Complexity: O(2n) ~ O(n)
# Space Complexity: O(n)
def length_of_longest_substring_better(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# ✅ Optimal Approach (Using HashMap for index tracking)
# -------------------------------------------------------
# Move left pointer to the right of the last occurrence of the current character
# Time Complexity: O(n)
# Space Complexity: O(n)
def length_of_longest_substring_optimal(s: str) -> int:
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
