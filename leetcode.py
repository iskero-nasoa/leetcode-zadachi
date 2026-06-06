# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#01/lune/2026
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, v1, v2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while v1 or v2 or carry:
            total = carry

            if v1:
                total += v1.val
                v1 = v1.next

            if v2:
                total += v2.val
                v2 = v2.next

            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next

        return dummy.next


def create_list(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

#02/june/2026
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

#03/june/2026
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

#04/june/2026
def is_poly(x):
    x = str(x)
    return x == x[::-1]

#05/june/2026
def skobki(x):
    neww = []
    for i in x:
        if i == "(" or i=="{" or i=="[" :
            neww.append(i)
        else:
            if not neww:
                return False
            last = neww.pop()
            if i == ")" and last != "(":
                return False
            if i == "]" and last != "[":
                return False
            if i == "}" and last != "{":
                return False
    return len(neww) == 0

#06/june/2026
def find_max(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest

#07/june/2026
def find_min(nums):
    lowest = nums[0]
    for i in nums:
        if i < lowest:
            lowest = i
    return lowest
