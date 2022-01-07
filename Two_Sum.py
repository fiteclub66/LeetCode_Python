# Two Sum
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Cameron's Solution.  Slower, but more memory efficient.  O(n^2)
        # for first_num in nums:
        #     remaining_nums = nums[(nums.index(first_num) + 1):len(nums)]
        #     for second_num in remaining_nums:
        #         if (first_num + second_num) == target:
        #             first_num_index = nums.index(first_num)
        #             second_num_index = remaining_nums.index(second_num) + first_num_index + 1
        #             return [first_num_index, second_num_index]


        # fastest solution.  Uses more memory, but O(n)
        hist = {}

        for index, num in enumerate(nums):
            if target - num in hist:
                return [hist[target - num], index]
            hist[num] = index



def main():
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(f'First Test: nums: {nums}, target: {target}')
    print(f'Output: {solution.twoSum(nums, target)}')
    nums = [3,3]
    target = 6
    print(f'First Test: nums: {nums}, target: {target}')
    print(f'Output: {solution.twoSum(nums, target)}')


if __name__ == "__main__":
    main()