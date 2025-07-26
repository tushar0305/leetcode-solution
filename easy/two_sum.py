"""
🔗 Problem: Two Sum
https://leetcode.com/problems/two-sum/description/

🧠 Level: Easy

🎯 Goal:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

Constraints:
- Exactly one solution exists.
- Cannot use the same element twice.

🧪 Examples:
Input: nums = [2,7,11,15], target = 9    => Output: [0,1]
Input: nums = [3,2,4], target = 6         => Output: [1,2]
Input: nums = [3,3], target = 6           => Output: [0,1]
"""

from typing import List

# 🚀 Brute Force Approach
# -----------------------------------
# Check every possible pair and return if the sum matches target.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# ⚡ Better Approach (Using Hash Map)
# -----------------------------------
# Store each number's index as we iterate.
# For each num, check if (target - num) exists in the map.
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_better(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# ✅ Optimal Approach
# -----------------------------------
# In this case, hash map approach is already optimal.
# If input is sorted, we can use two pointers. But LeetCode input isn't guaranteed to be sorted.
# So hash map = optimal for this problem.
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_optimal(nums: List[int], target: int) -> List[int]:
    return two_sum_better(nums, target)  # aliasing the optimal to better
