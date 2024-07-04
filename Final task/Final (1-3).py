def is_monotonic(nums):
    if not nums:
        return True

    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing


# Примеры из задания
print(is_monotonic([1, 2, 2, 3]))  # Output: true
print(is_monotonic([6, 5, 4, 4]))  # Output: true
print(is_monotonic([1, 3, 2]))  # Output: false

