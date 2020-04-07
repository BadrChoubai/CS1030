'''
Given a list of numbers like,
input_list [int] [1, 2, 3, 2, 5, 9, 9, 7, 2]

Write a program to create a dictionary where the key is the number and the value is the frequency of the number occuring in the
list
'''

nums: [int] = [1, 2, 3, 2, 5, 9, 9, 7, 2]
counter = dict()

for num in nums:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

print(input_list)
print(counter)
