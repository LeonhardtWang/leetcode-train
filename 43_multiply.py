class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0 for _ in range(len(num1)+len(num2))]
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                start = i + j - len(num1) - len(num2) + 1
                cur = int(num1[i]) * int(num2[j])
                carry = 0
                while cur or carry:
                    if cur:
                        res[start] += cur % 10 + carry
                        cur //= 10
                    else:
                        res[start] += carry
                    if res[start] > 10:
                        carry = res[start] // 10
                        res[start] %= 10
                    else:
                        carry = 0
                    start -= 1
        num = 0
        for r in res:
            num = num * 10 + r
        return str(num)
                
                
print(Solution().multiply("9211698838788156","9606088872226"))