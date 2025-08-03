def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        print(diff,"...........")
        if diff in seen:
            # print([seen[diff], i])
            return [seen[diff], i]
        seen[num] = i
        print(seen)


# nums = [4,4,6,3,1,66,8,5]
# target = 7

# res = two_sum(nums, target) 
# print(res)



def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i+1, len(nums)-1
        while l < r:
            print(l,i,r,".....inside")
            print(nums[l],nums[i],nums[r],".....inside _ values")
            s = nums[i] + nums[l] + nums[r]

            if s < 0: l += 1
            elif s > 0: r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1   #skips duplicate from l
                while l < r and nums[r] == nums[r-1]: r -= 1   #skips duplicate from r
                l += 1; r -= 1
        print(l,i,r,"outside")
        print(nums[l],nums[i],nums[r],".....insoutsideide")

    return res

# nums = [-1, 0, 1, 2, -1, -4,4]

# target = 7
# res = three_sum(nums)
# print(res)


def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            print(s[right],right,".right")
            print(s[left],left,"....left")
            print(char_set)
            char_set.remove(s[left])
            print(char_set)
            left += 1
        print("...........break")
        char_set.add(s[right])
        # print(char_set)
        # print(max_len, right-left+1)
        max_len = max(max_len, right - left + 1)

    return max_len

# s = "abcabcbb"
# s = "abcccddbaabcdefa"
# res = length_of_longest_substring(s)
# print(res)
# Step-by-step:
# - right = 0 → 'a' → add to set → window: "a"
# - right = 1 → 'b' → add to set → window: "ab"
# - right = 2 → 'c' → add to set → window: "abc" → max = 3
# - right = 3 → 'a' → duplicate → remove 'a', left = 1 → window: "bca"
# - continue...

# Final result: 3



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        # print(root.val)
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')


# Create the tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print("Inorder: ")
# inorder(root)       # Output: 4 2 5 1 3

# print("\nPreorder: ")
# preorder(root)      # Output: 1 2 4 5 3

# print("\nPostorder: ")
# postorder(root)     # Output: 4 5 2 3 1
