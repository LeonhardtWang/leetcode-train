class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                tmp = ''
                pop_char = stack.pop()
                while pop_char != '[':
                    tmp = pop_char + tmp
                    pop_char = stack.pop()
                num = ''
                while stack and '0' <= stack[-1] <= '9':
                    num_pop = stack.pop()
                    num = num_pop + num
                for p in tmp * int(num):
                    stack.append(p)
        return ''.join(stack)
            
                
print(Solution().decodeString("100[leetcode]"))