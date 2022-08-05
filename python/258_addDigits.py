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
        
        # 方法二：余九法(本题即为求数根)
        '''
        证明：
        假设，数d的根为d%9( 暂时不取0，整除时取9）
        当d < 10时，1~9这9个数肯定成立;
        当d >= 10时，d的根为d%9 = (d-1)%9+1，即d的前一个数的数根加1.
        得证.
        '''
        '''
        if num == 0:return 0
        return (num - 1) % 9 - 1
        '''