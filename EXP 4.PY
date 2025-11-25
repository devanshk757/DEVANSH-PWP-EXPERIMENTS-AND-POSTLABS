# import math
# c = list(range(1, 5, 1))
# result = math.prod(c)
# print(result) 

# numbers = [10, 24, 76, 23, 12]
# largest = max(numbers)
# print("The largest number is:", largest)

# my_list_1 = [5, 2, 90, 24, 10, 2, 90, 34]
# my_list_1 = list(dict.fromkeys(my_list_1))
# print(my_list_1)

# numbers = [1, 2, 2, 3, 3, 3, 3, 4]
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print(frequency)  

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common = list(set(list1) & set(list2))
# print(common)

nums = [1, 2, 3]
single_int = 0
for x in nums:
    single_int = single_int * 10 + x
print(single_int)  