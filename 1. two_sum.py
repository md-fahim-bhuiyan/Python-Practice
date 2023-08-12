#  Given an array of integers nums and an integer target, return indices of the
#  two numbers such that they add up to the target.
def two_sum(nums, target):
    seen = {}  # Dictionary to store seen numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        if complement in seen:
            return [seen[complement], i]  # Found a valid pair, return the indices
        seen[num] = i  # Add the current number to the dictionary
    return None  # No valid pair found

# Example usage:
nums = [1, 7, 8, 15]
target = 15
result = two_sum(nums, target)
print(result)
