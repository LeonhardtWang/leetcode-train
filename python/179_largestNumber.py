class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        def compare(a, b):
            return int(str(a)+str(b)) - int(str(b)+str(a))
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        return ''.join([str(num) for num in nums]) if nums[0] != 0 else '0'