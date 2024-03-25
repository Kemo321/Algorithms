# Generates next permutation

def nextPermutation(self, nums: list[int]) -> None:
    # Do not return anything, modify nums in-place instead.
    if len(nums) == 2:
        nums.reverse()
        return
    if len(nums) < 2:
        return
    # If highest possible number - reverse by sorting
    if nums == (sorted(nums))[::-1]:
        nums.sort()
        return
    # initialize two pointers
    right = len(nums) - 1
    left = right - 1
    # Initialize swap pointers
    left_swap = 0
    right_swap = 0
    # Look for the indexes to swap
    while left >= 0:
        if nums[left] < nums[right]:
            if left > left_swap or right > right_swap:
                left_swap = left
                right_swap = right
        if left == 0:
            right -= 1
            left = right - 1
        else:
            left -= 1
    # Swap indexes
    nums[right_swap], nums[left_swap] = nums[left_swap], nums[right_swap]
    # Sort the list from the left_swap to the end
    nums[left_swap + 1:] = sorted(nums[left_swap + 1:])
