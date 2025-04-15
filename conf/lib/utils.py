# Question 1: Reverse a Linked List
# Problem: Write a function to reverse a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print("Original Linked List:")
ll.print_list()
ll.reverse()
print("Reversed Linked List:")
ll.print_list()

# Question 2: Find the First Non-Repeating Character in a String
# Problem: Write a function to find the first non-repeating character in a string.

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Example usage:
string = "swiss"
result = first_non_repeating_char(string)
print(f"First non-repeating character in '{string}': {result}")

# Question 3: Implement Binary Search
# Problem: Write a function to perform binary search on a sorted array.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
sorted_array = [1, 3, 5, 7, 9, 11]
target = 7
index = binary_search(sorted_array, target)
print(f"Index of {target} in the array: {index}")