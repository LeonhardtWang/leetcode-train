class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 方法一：递归
        sum_num = 0
        for i in str(num):
            sum_num += int(i)
        if sum_num < 10:
            return sum_num
        else:
            return self.addDigits(sum_num)
        
        # 方法二：余九法
        '''
        if num == 0:return 0
        return (num - 1) % 9 - 1
        '''