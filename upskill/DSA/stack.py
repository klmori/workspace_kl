class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def traverse(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.top.data

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        popped_value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_value



def reverse_string(s):
    stack = Stack()
    
    for char in s:
        stack.push(char)
    
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

def text_editor(text, pattern):
    u = Stack()
    r = Stack()

    for i in text:
        u.pusjh(i)
    
    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        elif i == 'r':
            data = r.pop()
            u.push(data)     

    res = ""

    while not u.is_empty():
        res += u.pop()+""
        
# Example usage
if __name__ == "__main__":  
    input_string = "Hello, World!"
    reversed_string = reverse_string(input_string)
    print(f"Original String: {input_string}")
    print(f"Reversed String: {reversed_string}")