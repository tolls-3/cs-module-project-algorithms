'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_list = []
    for i in range(len(nums)):
        if k <= len(nums):
            new_arr = nums[i:k]
            k += 1
            maximum_num = max(new_arr)
            max_list.append(maximum_num)

    return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
