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

#08/june/2026
def count_even(x):
    answer = 0
    for i in x:
        if i%2 == 0:
            answer += 1
    return answer


#09/june/2026
def Majority(x):
    answer = {}
    for i in x:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
    for y in answer:
        if answer[y] > len(x) / 2:
            return y


#10/june/2026
def second_largest(x):
    largest = find_max(x)
    answer = None

    for i in x:
        if i != largest:
            if answer is None:
                answer = i
            elif i > answer:
                answer = i 
    return answer

#11/june/2026
def count_occurrences(nums, target):
    accurences = 0
    for i in nums:
        if i == target:
            accurences += 1
    return accurences


#12/june/2026
def positive_sum(nums):
    answer = 0
    for i in nums:
        if i > 0:
            answer += i
    return answer


#13/june/2026
def first_negative(nums):
    for i in nums:
        if i < 0:
            return i
    return None


#14/june/2026
def missingNumber(nums):
    n = len(nums)
    e = n * (n + 1) // 2
    a = sum(nums)
    return e - a


#15/june/2026
def first_positive(nums):
    for i in range(len(nums)):
        if nums[i] > 0:
            return i
        

#16/june/2026
def last_positive(nums):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > 0:
            return i
        

#17/june/2026
def max_profit(prices):
    minn = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] < minn:
            minn = prices[i]
        pprofit = max(prices[i:]) - prices[i]
        if pprofit > profit:
            profit = pprofit
    return profit


#18/june/2026
def product_except_self(nums):
    answer = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product *= nums[j]
        answer.append(product)


#19/june/2026
def longest_word(words):
    longest = words[0]
    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest


#20/june/2026
def is_anagram(f, s):
    first = {}
    second = {}
    for i in f:
        if i in first:
            first[i] += 1
        else:
            first[i] = 1
    for i in s:
        if i in second:
            second[i] += 1
        else:
            second[i] = 1
    return first == second


#21/june/2026
def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())


#22/june/2026
def top_k_freq(nums, k):
    num = {}
    for i in nums:
        if i not in num:
            num[i] = 1
        else:
            num[i] += 1
    pairs = list(num.items())
    pairs.sort(key=lambda x: x[1], reverse=True)
    answer = []

    for i in range(k):
        answer.append(pairs[i][0])
    return answer


#23/june/2026
def longest_consecutive(nums):
    if not nums:
        return 0

    numbers = set(nums)
    longest = 0

    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1
            while current + 1 in numbers:
                current += 1
                length += 1
            if length > longest:
                longest = length
    return longest


#24/june/2026
def daily_temperatures(temperatures):
    answer = []
    for i in range(len(temperatures)):
        days = 0
        found = False
        for j in range(i + 1, len(temperatures)):
            days += 1
            if temperatures[j] > temperatures[i]:
                answer.append(days)
                found = True
                break
        if not found:
            answer.append(0)

    return answer


#25/june/2026
def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        if area > best:
            best = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


#26/june/2026
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#27/june/2026
def max_profit(prices):
    min_price = prices[0]
    best_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > best_profit:
            best_profit = profit
    return best_profit


#28/june/2026
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next   
        current.next = prev        
        prev = current            
        current = next_node       

    return prev


#29/june/2026
def num_islands(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)  
        dfs(r - 1, c)  
        dfs(r, c + 1)
        dfs(r, c - 1)  
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


#30/june/2026
def kth_largest(nums, k):
    neww = sorted(nums, reverse=True)
    return neww[k-1]


#01/july/2026
def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for interval in intervals[1:]:
        last = merged[-1]
        if interval[0] <= last[1]:
            last[1] = max(last[1], interval[1])
        else:
            merged.append(interval)
    return merged


#02/july/2026
def move_zeroes(nums):
    non_zero = []
    zero_count = 0
    for i in nums: 
        if i != 0:
            non_zero.append(i)
        else: 
            zero_count += 1
    for y in range(zero_count):
        non_zero.append(0)
    return non_zero


#03/july/2026
def find_missing_num(nums):
    nums = sorted(nums)
    if nums[0] != 0:
        return 0
    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i] + 1:
            return nums[i] + 1
    return len(nums)


#04/july/2026
def reverse_string(x):
    answer = ""
    for i in range(len(x) - 1, -1, -1):
        answer += x[i]
    return answer


#05/july/2026
def remove_duplicates(nums):
    answer = []
    for i in nums:
        if i not in answer:
            answer.append(i)
    return answer


#06/july/2026
def find_difference(s, t):
    letters = {}
    for i in s:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    for i in t:
        if i not in letters:
            return i
        letters[i] -= 1
        if letters[i] < 0:
            return i
        

#07/july/2026
def find_max_consecutive_ones(nums):
    current = 0
    best = 0
    for i in nums:
        if i == 1:
            current += 1
            if current > best:
                best = current
        else:
            current = 0
    return best


#08/july/2026
def contains_nearby_duplicate(nums, k):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            if i - seen[nums[i]] <= k:
                return True
        seen[nums[i]] = i
    return False


#09/july/2026
def intersection(nums1, nums2):
    answer = []
    for i in nums1:
        if i in nums2 and i not in answer:
            answer.append(i)
    return answer