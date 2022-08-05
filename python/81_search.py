class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        length = len(nums)
        if length == 0:
            return False
        split = None
        for i, num in enumerate(nums):
            if i + 1 <= len(nums) - 1 and nums[i] > nums[i+1]:
                split = i # 旋转点
                break
        lo = 0 
        hi = length - 1 # 假设为升序数组
        while lo <= hi:
            mid = (lo + hi) // 2
            
            # 转换成原数组的索引
            if split is not None:
                mid = self.rank_to_orgin(mid, length, split)
                
            if nums[mid] > target:
                if split is not None:
                    mid = self.orgin_to_rank(mid, length, split) # 转换成升序数组的索引
                hi = mid - 1
            elif nums[mid] < target:
                if split is not None:
                    mid = self.orgin_to_rank(mid, length, split) # 转换成升序数组的索引
                lo = mid + 1
            else:
                return True
        return False
    
    def orgin_to_rank(self, index, length, split):
        if 0 <= index <= split:
            return index + length - split - 1
        else:
            return index - split - 1
    
    def rank_to_orgin(self, index, length, split):
        if length - split - 1 <= index <= length - 1:
            return index -length + split + 1
        else:
            return index + split + 1
                
        
        