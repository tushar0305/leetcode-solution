"""
🔗 Problem: Integer to Roman
https://leetcode.com/problems/integer-to-roman/

🧠 Level: Medium

🎯 Goal:
Given an integer `num`, convert it to a Roman numeral.

Only values from 1 to 3999 are valid input (based on the problem constraint).

🧪 Example:
Input: num = 3749
Output: "MMMDCCXLIX"

Explanation breakdown:
3000 = MMM
 700 = DCC
  40 = XL
   9 = IX
=> MMMDCCXLIX
"""

# ✅ Optimal Solution (Greedy with Value Mapping)
# -----------------------------------------------
# Loop through values from largest to smallest and subtract repeatedly.
# Time Complexity: O(1) – Since input range is fixed (1 to 3999)
# Space Complexity: O(1)
def int_to_roman_optimal(num: int) -> str:
    val_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
        (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
        (1, 'I')
    ]

    result = []
    for val, roman in val_to_roman:
        while num >= val:
            result.append(roman)
            num -= val

    return ''.join(result)

# Alias brute/better to optimal as there's only one meaningful way
def int_to_roman_better(num: int) -> str:
    return int_to_roman_optimal(num)

def int_to_roman_bruteforce(num: int) -> str:
    return int_to_roman_optimal(num)
