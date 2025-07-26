"""
🔗 Problem: Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/

🧠 Level: Medium

🎯 Goal:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Return the sum as a linked list (also in reverse order).

🧪 Examples:
Input: l1 = [2,4,3], l2 = [5,6,4]    => Output: [7,0,8]     (342 + 465 = 807)
Input: l1 = [0], l2 = [0]            => Output: [0]
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] => Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 🚀 Brute Force Approach (Simulate digit-by-digit addition)
# ----------------------------------------------------------
# Traverse both lists while adding corresponding digits.
# Keep track of carry for sums >= 10.
# Time Complexity: O(max(n, m)) where n and m are lengths of l1 and l2.
# Space Complexity: O(max(n, m)) for result list.
def add_two_numbers_bruteforce(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# ⚡ Better / Optimal Approach
# ----------------------------
# The above approach is already optimal in terms of both time and space.
# There's no better way unless extra memory constraints are imposed or inputs are huge.
# So we alias it for consistency.
def add_two_numbers_optimal(l1: ListNode, l2: ListNode) -> ListNode:
    return add_two_numbers_bruteforce(l1, l2)
