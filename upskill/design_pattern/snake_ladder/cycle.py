# Create this list:
# 1 → 2 → 3 → 4 → 2 (cycle back to node with value 2)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Creating nodes
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

# Link them
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2  # cycle here!
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(has_cycle(n1))  # Output: True ✅


# 0 → 1 → 2 → 0   # cycle
graph = {
    0: [1],
    1: [2],
    2: [0]  # back to 0 = cycle!
}
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor): return True
            elif neighbor in rec_stack:
                return True  # Cycle found

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

print(has_cycle_directed(graph))  # Output: True ✅
