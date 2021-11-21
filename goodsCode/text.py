# num = "9"
# ascii_num = ord(num)
# cnt = ascii_num - ord("0")
# print(ascii_num)
# print(cnt)
# print(3*"M")
# dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, 
#                   "C": 100, "D": 500, "M": 1000} 

# def quicksort(array):
#     if len(array)<=1:
#         return array
#     pivot = len(array)//2
#     left = [item  for item in array if item < array[pivot]]
#     right = [item  for item in array if item > array[pivot]]
#     mid = [item  for item in array if item ==array[pivot]]


# lst = [1,2]
# print(lst[2::])

# print("V" in dict_roman)


# # a = (1<<31) - 1
# # print(a)
# # dic = ["2", 0]
# # print(dict(dic))

# word_dict = {}
# words = ["foo","bar"]
# for word in words:
#     if word in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1
# print(word_dict)

# dump = word_dict.copy()
# print(dump)

# a = [1,2,3,4,4]
# reversed(a)
# print(reversed(a))

# print(1//2)

# def correct(sub_s):
#     stack = []
#     for i in sub_s:
#         if i == "(":
#             stack.append(i)
#         elif stack != [] and i == ")":
#             stack.pop()
#         else:
#             return False
#     if stack == []:
#         return True
#     else:
#         return False

# def judge(nums):
#     point1 = 0
#     point2 = len(nums) - 1
#     while point2-point1 != 1:
#         low = (point1+point2) // 2
#         if nums[low] < nums[point2]:
#             p2 =low
#         elif nums[low] > nums[point2]:
#             p1 = low
#     return nums[low]
# print(judge([1,2,3]))

# def dichotomy(lst,target):
#     p1 = 0
#     p2 = len(lst)-1
#     mid = len(lst) // 2
#     while p1 <= p2:
#         if target > lst[mid]:
#             p1 = mid+1
#         elif target < lst[mid]:
#             p2 = mid-1
#         else:
#             return mid
#         mid = (p1+p2)//2
#     return -1
    
# print(dichotomy([0,1,3,4,5,6],6))
# print(ord("."))

# s = ""
# count = 2
# currentStr = "1"
# s += str(count) + currentStr
# print(s)


# s = [[2,2,2,2],[2,3,3],[2,6],[3,2,3],[3,3,2],[6,2]]
# s = [1,2,3,4]
# print(str(s))
# print((1 << 31) - 1)
# print(2 ** 31)
# for i in range(4,-1,-1):
#     print(i)
# a = "0"*3
# print(2<<10)
# a = True
# b = False
# c = b or a
# print(c)

# 


# def rotate(matrix):
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     # transpose row to column
#     i = 0
#     j = 0
#     while i != len(matrix):
#         if j == len(matrix):
#             i += 1
#             j = i
#         else:
#             change = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = change
#             j += 1

# def rotate222(matrix):
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     # transpose row to column
#     m = 0
#     left = 0
#     right = len(matrix)-1
#     while m != len(matrix):
#         if left == right or left -right == 1:
#             left = 0
#             right = len(matrix)-1
#             m += 1
#         else:
#             help = matrix[m][left]
#             matrix[m][left] = matrix[m][right]
#             matrix[m][right] = help
#             left += 1
#             right -= 1
# a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# rotate(a)
# rotate222(a)
# print(a)
# strs = "asdf"
# lst_strs = list(strs)
# lst_strs.sort()
# s = "".join(lst_strs)
# print(s)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# dic = {}
# for st in strs:
#     lst_st = list(st)
#     lst_st.sort()
#     key = "".join(lst_st)
#     if key in dic:
#         dic[key] += [st]
#     else:
#         dic[key] = [st]
# print(dic)
# print(int('10111', 2))
# bin(100.1001)

# st = "z"
# ascii_i = ord(st)
# print(type(ascii_i-96))
# a = ["Q", ".", ".", "."]
# print(str(a))
# a = "...."
# a[1] = "A"
# print(a)
# queen = [None] * 8
# print(queen)
# a = [1,1,1]
# b = a[0:1]
# print(b)
# a = 0
# b = 9
# a, b = b, a
# print(a, b)
# def quickSort(lists):
#     if len(lists) < 2:
#         return lists
#     else:
#         pivot = lists[0]
#         left = [lst for lst in lists[1:] if lst[0] <= pivot[0]]
#         right = [lst for lst in lists[1:] if lst[0] > pivot[0]]
#         return quickSort(left) + [pivot] + quickSort(right)
# s = quickSort([[9,2], [8,7], [1,2], [6,10]])
# print(s)


# matrix = [[None for _ in range(n)] for _ in range(n)]
# print(matrix)
# print(float(1e-6))
# ub = [1]

# print(ub+[9])
# import numpy as np 
# a = np.array([1,2,3])  
# print (a)
# def quickSort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = []
#         big = []
#         for i in arr[1:]:
#             if i <= pivot:
#                 less.append(i)
#             else:
#                 big.append(i)
#         return quickSort(less) + [pivot] + quickSort(big)
    
# print(quickSort([1,2,4,2,1,3,5,4]))

print(int(-0.111))
print(6 // (-12))