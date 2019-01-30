class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 方法一：暴力方法，超时
        '''
        length = len(nums)
        if length <= 1:
            return False
        fi = 0
        judge = False # 判断是否存在相等的情况
        while fi <= length - 2:
            si = fi + 1
            while si <= length -1 :
                if nums[fi] == nums[si]:
                    if si - fi <= k: # 判断i和j的差的绝对值是否满足最大为k
                        return True
                    else:
                        si += 1
                else:
                    si += 1
            fi += 1
        return judge
        '''
        
        # 方法二：用字典存储索引，然后进行判断
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                record[nums[i]].append(i)
            else:
                record[nums[i]] = [i]
        for _, values in record.items():
            if len(values) >= 2:
                f = 0
                while f <= len(values) - 2:
                    if values[f+1] - values[f] <= k:
                        return True
                    else:
                        f += 1
        return False
    