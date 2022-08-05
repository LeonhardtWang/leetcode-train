# 方法一：双队列
class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        stack1 = deque() # 储存数字
        stack2 = deque() # 储存符号
        index = 0
        while index < len(s):
            curr, index = self._helper(s, index)
            if curr == '':
                break
            if isinstance(curr, int):
                stack1.append(curr)
            elif curr == '*':
                next_num, index = self._helper(s, index)
                stack1.append(stack1.pop() * next_num)
            elif curr == '/':
                next_num, index = self._helper(s, index)
                stack1.append(stack1.pop() // next_num)
            else:
                stack2.append(curr)
        while stack2:
            sign = stack2.popleft()
            num1, num2 = stack1.popleft(), stack1.popleft()
            if sign == '-':
                stack1.appendleft(num1-num2)
            else:
                stack1.appendleft(num1+num2)
        return stack1[-1]  
                
    def _helper(self, s, index):
        # 取出一个数字或运算符
        curr_char = ''
        while index < len(s) and s[index] == ' ':
            index += 1
        if index >= len(s):
            return '', index
        while index < len(s) and '0' <= s[index] <= '9':
            curr_char += s[index]
            index += 1
        if curr_char:
            return int(curr_char), index
        if s[index] in {'+', '-', '*', '/'}:
            return s[index], index+1


# 方法二：递归（超内存） ->改为引用传参(递归过深,python最大递归深度998)
class Solution2:
    def calculate(self, s: str) -> int:
        s = ''.join([ch for ch in s if ch != ' ']) # 去空格
        return self.Core(s, 0, len(s))
    
    def Core(self, s, index, length):
        pos_neg = 1 # 判断正负
        if s[index] == '-':
            pos_neg = -1
            index += 1
        num, index = self.get_num(s, index, length)
        if index >= length:
            return num * pos_neg
        sign = s[index]
        while sign in {'*', '/'}:
            next_num, index = self.get_num(s, index+1, length)
            if sign == '*':
                num *= next_num
            else:
                num //= next_num
            if index >= length:
                return num * pos_neg
            sign = s[index]
        if sign == '+':
            index += 1
        return num * pos_neg + self.Core(s, index, length)
        
    def get_num(self, s, index, length):
        # 取数
        curr = ''
        while index < length and '0' <= s[index] <= '9':
            curr += s[index]
            index += 1
        return int(curr), index

print(Solution2().calculate("1+7-7+3+3+6"))