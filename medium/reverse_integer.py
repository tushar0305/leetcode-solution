"""
🔗 Problem: Reverse Integer
https://leetcode.com/problems/reverse-integer/

🧠 Level: Medium

🎯 Goal:
Given a signed 32-bit integer `x`, return the reversed digits of `x`.
Return 0 if the reversed value overflows the 32-bit signed integer range.

Valid range: [-2^31, 2^31 - 1] = [-2147483648, 2147483647]

🧪 Examples:
Input: x = 123     => Output: 321
Input: x = -123    => Output: -321
Input: x = 120     => Output: 21
"""

INT_MIN = -2**31
INT_MAX = 2**31 - 1

# 🚀 Brute Force (Convert to string, reverse, and convert back)
# -------------------------------------------------------------
# Time Complexity: O(n), where n is the number of digits in x
# Space Complexity: O(n) for string manipulation
def reverse_integer_bruteforce(x: int) -> int:
    sign = -1 if x < 0 else 1
    reversed_str = str(abs(x))[::-1]
    reversed_int = sign * int(reversed_str)

    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0
    return reversed_int

# ⚡ Better Approach (Mathematical, no string conversion)
# --------------------------------------------------------
# Time Complexity: O(log10(x)) ~ O(n) digits
# Space Complexity: O(1)
def reverse_integer_better(x: int) -> int:
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        # Check for overflow before appending digit
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    return sign * result

# ✅ Optimal = Better for this problem
def reverse_integer_optimal(x: int) -> int:
    return reverse_integer_better(x)
