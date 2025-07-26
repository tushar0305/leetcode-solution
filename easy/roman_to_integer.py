"""
🔗 Problem: Roman to Integer
https://leetcode.com/problems/roman-to-integer/

🧠 Level: Easy

🎯 Goal:
Given a Roman numeral string `s`, convert it to an integer.

🧪 Examples:
Input: s = "III"         => Output: 3
Input: s = "LVIII"       => Output: 58  (L=50, V=5, III=3)
Input: s = "MCMXCIV"     => Output: 1994 (M=1000, CM=900, XC=90, IV=4)
"""

# ✅ Optimal Solution (Right-to-left traversal with subtractive logic)
# ---------------------------------------------------------------
# Rule: if current value < previous, subtract it. Otherwise, add it.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value

        return total
