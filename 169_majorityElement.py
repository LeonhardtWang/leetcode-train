class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_num = {}
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                dict_num[num] += 1
        sort_dict_num = sorted(dict_num.items(), key=lambda s: s[1])
        return sort_dict_num[-1][0]

        # 方法二
        count = 0
        num_temp = 0
        for num in nums:
            if not num_temp:
                num_temp = num
                count += 1
            elif num == num_temp:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num_temp = num
                    count = 1
        return num_temp