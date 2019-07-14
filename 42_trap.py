# 暴力法
class Solution:
    def trap(self, height: list) -> int:
        res = 0
        if not height:
            return res
        max_height = max(height)
        for h in range(max_height, 0, -1):
            i_lis = []
            for i, hh in enumerate(height):
                if hh >= h:
                    i_lis.append(i)
            del_index = []
            i = 0
            while i < len(i_lis)-1:
                dis = [i_lis[i], i_lis[i+1]]
                for j in range(dis[0]+1, dis[1]):
                    res += h - height[j]
                    del_index.append(j)
                i += 1
            height = [height[i] for i in range(len(height)) if i not in del_index]
        return res

# 遍历数组，当前height下，累加左边最大值和右边最大值中的最小值减去当前height（包括本身）
class Solution2:
    def trap(self, height: list) -> int:
        left_max_index = [0 for _ in range(len(height))]
        right_max_index = [0 for _ in range(len(height))]
        for i in range(len(height)):
            if i == 0:
                left_max_index[i] = i
            else:
                if height[i] > height[left_max_index[i-1]]:
                    left_max_index[i] = i
                else:
                    left_max_index[i] = left_max_index[i-1]
            
            j = len(height) - i - 1
            if j == len(height) - 1:
                right_max_index[j] = j
            else:
                if height[j] > height[right_max_index[j+1]]:
                    right_max_index[j] = j
                else:
                    right_max_index[j] = right_max_index[j+1]
        
        res = 0
        for i in range(len(height)):
            res += min(height[left_max_index[i]], height[right_max_index[i]]) - height[i]
        return res


print(Solution2().trap([5,4,1,2]))