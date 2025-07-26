"""
🔗 Problem: Palindrome Number
https://leetcode.com/problems/palindrome-number/

🧠 Level: Easy

🎯 Goal:
Given an integer `x`, return `True` if it is a palindrome; otherwise, return `False`.

A palindrome is a number that reads the same backward as forward.

🧪 Examples:
Input: x = 121     => Output: True
Input: x = -121    => Output: False  (negative sign makes it non-palindromic)
Input: x = 10      => Output: False  ("01" ≠ "10")
"""

# 🚀 Brute Force (Convert to string and reverse)
# ---------------------------------------------
# Time Complexity: O(n), where n is the number of digits
# Space Complexity: O(n), due to string conversion
def is_palindrome_bruteforce(x: int) -> bool:
    return str(x) == str(x)[::-1]

# ⚡ Better Approach (Early checks and integer operations)
# --------------------------------------------------------
# Check for negatives and trailing zeroes.
# Reverse the number and compare.
# Time Complexity: O(log10(x)) ~ O(n digits)
# Space Complexity: O(1)
def is_palindrome_better(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For odd-length numbers, remove the middle digit using //
    return x == reversed_half or x == reversed_half // 10

# ✅ Optimal = Better for this problem
def is_palindrome_optimal(x: int) -> bool:
    return is_palindrome_better(x)
