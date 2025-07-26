"""
🔗 Problem: LFU Cache (Leetcode 460)
https://leetcode.com/problems/lfu-cache/

🧠 Level: Hard

🎯 Goal:
Design a data structure that works like a cache and removes the **Least Frequently Used** key when full.
If multiple keys have the same frequency, remove the **Least Recently Used** among them.

Requirements:
- `get(key)` and `put(key, value)` must run in **O(1)** average time complexity.

🧪 Example:
LFUCache lfu = LFUCache(2)
lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1)      # return 1; cnt(1)=2
lfu.put(3, 3)   # evict 2 (LFU); cache=[3,1]
lfu.get(2)      # return -1
lfu.get(3)      # return 3; cnt(3)=2
lfu.put(4, 4)   # evict 1 (tie LFU, LRU); cache=[4,3]
lfu.get(1)      # return -1
lfu.get(3)      # return 3
lfu.get(4)      # return 4
"""

from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    # ✅ Get value and update frequency
    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._update_freq(key)
        return self.key_to_val[key]

    # ✅ Insert or update value and manage eviction
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.capacity:
            # Evict LFU key (with LRU tie-break)
            lfu_keys = self.freq_to_keys[self.min_freq]
            evict_key, _ = lfu_keys.popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        # Insert new key with freq 1
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    # 🔁 Internal helper to update frequency
    def _update_freq(self, key: int):
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None
