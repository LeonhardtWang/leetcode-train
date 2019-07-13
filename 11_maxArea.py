class Solution:
    def maxArea(self, height: list) -> int:
        i = 0
        j = len(height) - 1
        max_water = 0
        while i < j:
            tmp = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            if tmp > max_water:
                max_water = tmp
        return max_water
        
if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))