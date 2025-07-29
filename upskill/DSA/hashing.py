# class HashingDSAExamples:

#     @staticmethod
#     def has_duplicates(arr):
#         seen = set()
#         for num in arr:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False

#     @staticmethod
#     def frequency_count(arr):
#         freq = {}
#         for item in arr:
#             freq[item] = freq.get(item, 0) + 1
#         return freq

#     @staticmethod
#     def two_sum(nums, target):
#         index_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in index_map:
#                 return [index_map[complement], i]
#             index_map[num] = i
#         return []

# class HashTable:
#     def __init__(self):
#         self.size = 10
#         self.table = [[] for _ in range(self.size)]

#     def _hash(self, key):
#         return hash(key) % self.size

#     def put(self, key, value):
#         idx = self._hash(key)
#         for pair in self.table[idx]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[idx].append([key, value])

#     def get(self, key):
#         idx = self._hash(key)
#         for pair in self.table[idx]:
#             if pair[0] == key:
#                 return pair[1]
#         return None

#     def remove(self, key):
#         idx = self._hash(key)
#         self.table[idx] = [pair for pair in self.table[idx] if pair[0] != key]


# # ------------------ Usage ------------------ #

# # 1. Duplicate check
# print(HashingDSAExamples.has_duplicates([1, 2, 3, 2]))  # True

# # 2. Frequency counter
# print(HashingDSAExamples.frequency_count(['a', 'b', 'a', 'b', 'c']))

# # 3. Two sum
# print(HashingDSAExamples.two_sum([2, 7, 11, 15], 9))  # [0, 1]

# # 4. Hash table demo
# ht = HashTable()
# ht.put("apple", 10)
# ht.put("banana", 5)
# print(ht.get("banana"))  # 5
# ht.remove("banana")
# print(ht.get("banana"))  # None





class Dictionary:

  def __init__(self, size):
    self.size = size
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self, key, value):
    hash_value = self.hash_function(key)

    if self.slots[hash_value] == None:
      self.slots[hash_value] = key
      self.data[hash_value] = value

    else:

      if self.slots[hash_value] == key:
        self.data[hash_value] = value
      else:
        new_hash_value = self.rehash(hash_value)

        while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
          new_hash_value = self.rehash(new_hash_value)

        if self.slots[new_hash_value] == None:
          self.slots[new_hash_value] = key
          self.data[new_hash_value] = value
        else:
          self.data[new_hash_value] = value

  def get(self, key):
    start_position = self.hash_function(key)
    current_position = start_position

    while self.slots[current_position] != None:

      if self.slots[current_position] == key:
        return self.data[current_position]
      
      current_position = self.rehash(current_position)

      if current_position == start_position:
        return "Not Found"

    return "None wala Not Found"

  def __str__(self):

    for i in range(len(self.slots)):
      if self.slots[i] != None:
        print(self.slots[i],":",self.data[i],end=' ')

    return ""

  def __getitem__(self,key):
    return self.get(key)

  def __setitem__(self,key,value):
    self.put(key,value)
  
  def rehash(self, old_hash):
    return (old_hash + 1) % self.size


  def hash_function(self, key):

    return abs(hash(key)) % self.size


D1 = Dictionary(3)
D1['python'] = 56
D1['c'] = 1000
print(D1.slots)
print(D1.data)
print(D1.__getitem__('python'))
print(D1.__getitem__('c'))