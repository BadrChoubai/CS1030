# These a are problems related to what we covered in class about lists
# 
# Because python is dynamically typed, lists can have mixed values 
#
# Define a list:
#   my_list = []
#   my_mixed_value_list = ["string", 1, True]
#
# Access a value in a list:
#
#   boolean = my_mixed_value_list[2]
#

def list_iteration():

    my_number_list = [1, 2, 3]

    for num in my_number_list:
        print(num)

def find_max_value(nums: [int]) -> int:

    largest = nums[0] 
  
    for num in nums:
        if num >= largest:
            largest = num

    return largest, min(nums)

def main():
    list_iteration() 

    nums = [-10, 2, 3, 42.91, -14, 10, 8, 34.2]
    largest_num = find_max_value(nums)
    print(largest_num)

if __name__ == "__main__":
    main()
