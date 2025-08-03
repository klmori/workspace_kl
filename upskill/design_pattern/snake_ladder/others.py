import heapq

def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)  # min heap

    for n in nums[k:]:
        if n > heap[0]:
            heapq.heappushpop(heap, n)

    return heap[0]
nums = [3,2,1,5,6,4]
k = 2
Output: 5  # [6,5] → 2nd largest = 5



def max_sum_subarray(nums, k):
    max_sum = curr_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        print(i)
        print(nums[i], nums[i-k])
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum
nums = [2,1,5,1,3,2]
k = 3
max_sum_subarray(nums, k)
# Subarrays of size 3: [2,1,5], [1,5,1], [5,1,3], [1,3,2]
# Max sum = 9 → [5,1,3]



from collections import defaultdict

words = ["bat", "tab", "eat", "tea"]
groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

# Output: {"abt": ["bat", "tab"], "aet": ["eat", "tea"]}


from collections import Counter

nums = [1, 2, 2, 3]
counts = Counter(nums)
# Output: {1:1, 2:2, 3:1}
