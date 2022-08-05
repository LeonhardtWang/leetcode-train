class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_ptr, right_ptr = 0, len(numbers) - 1
        while left_ptr < right_ptr:
            sum_l_and_r = numbers[left_ptr] + numbers[right_ptr]
            if sum_l_and_r > target:
                right_ptr -= 1
            elif sum_l_and_r < target:
                left_ptr += 1
            else:
                return [left_ptr+1, right_ptr+1]
        return None