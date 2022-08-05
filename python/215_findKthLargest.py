# 方法一：小顶堆（每个结点的值都大于或等于其左右孩子结点的值）
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 标准库
        # import heapq
        # return heapq.nlargest(k, nums)[-1]
        
        # 维护一个只有K个节点的小顶堆
        class Heap(object):
            def __init__(self, nums, k):
                self.heap = []
                self.k = k
                for num in nums:
                    self.insert(num)
                    
            def insert(self, num):
                if len(self.heap) < self.k:
                    self.heap.append(num)
                    self._upfilter()   
                else:
                    if self.heap[0] < num:
                        self.remove()
                        self.heap.append(num)
                        self._upfilter()
                    
            def _upfilter(self):
                # 刚插入的元素上滤过程
                insert_i = len(self.heap) - 1
                parent_i = (insert_i + 1) // 2 - 1 # 刚插入元素对应的父节点索引
                while parent_i >=0 and self.heap[insert_i] < self.heap[parent_i]:
                    # 开始上滤（交换）
                    tmp = self.heap[insert_i]
                    self.heap[insert_i] = self.heap[parent_i]
                    self.heap[parent_i] = tmp
                    insert_i = parent_i
                    parent_i = (insert_i + 1) // 2 - 1
                    
            def _downfilter(self):
                # 下滤过程
                key_i = 0
                len_heap = len(self.heap) - 1
                while 2 * key_i + 1 <= len_heap:
                    left_i = 2 * key_i + 1
                    right_i = 2 * key_i + 2
                    is_change = False
                    if (left_i <= len_heap and right_i <= len_heap and 
                        self.heap[key_i] > min(self.heap[left_i], self.heap[right_i])):
                        exc_i = (left_i, right_i)[self.heap[left_i]>=self.heap[right_i]]
                        is_change = True
                    if (left_i <= len_heap and right_i > len_heap and 
                        self.heap[key_i] > self.heap[left_i]):
                        exc_i = left_i
                        is_change = True
                    if not is_change:
                        break
                    self.heap[key_i], self.heap[exc_i] = self.heap[exc_i], self.heap[key_i]
                    key_i = exc_i    
                
            def remove(self):
                # 删除堆顶元素
                # 先交换堆顶和末尾元素，删除末尾元素，再启动下滤过程
                self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
                self.heap.pop()
                self._downfilter()
            
            def get_min(self):
                return self.heap[0]
                        
        heap = Heap(nums, k)
        return heap.get_min()

# 方法二：利用快速排序的思想
class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self._quick_sort(nums, 0, len(nums)-1, k)

    def _quick_sort(self, nums, left, right, k):
        if left == right:
            return nums[left]
        pivot = left
        l = left + 1
        r = right
        while l < r:
            while nums[l] <= nums[pivot] and l < r:
                l += 1
            while nums[r] >= nums[pivot] and l < r:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            
        if nums[l] <= nums[pivot]:
            nums[pivot], nums[l] = nums[l], nums[pivot]
            pivot = l 
        else:
            nums[pivot], nums[l-1] = nums[l-1], nums[pivot]
            pivot = l - 1

        if pivot < len(nums) - k:
            return self._quick_sort(nums, pivot+1, right, k)
        elif pivot > len(nums) - k:
            return self._quick_sort(nums, left, pivot-1, k)
        else:
            return nums[pivot]

# 快速排序（版本一）
def quick_sort(nums, left, right):
    if left >= right:
        return 
    pivot = left 
    l = left + 1
    r = right
    while l < r:
        while nums[l] <= nums[pivot] and l < r:
            l += 1
        while nums[r] >= nums[pivot] and l < r:
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]
    if nums[l] <= nums[pivot]:
        nums[pivot], nums[l] = nums[l], nums[pivot]
        pivot = l 
    else:
        nums[pivot], nums[l-1] = nums[l-1], nums[pivot]
        pivot = l - 1
    quick_sort(nums, left, pivot-1)
    quick_sort(nums, pivot+1, right)


# 快速排序（版本二）
def quick_sort2(array):
    def recursive(begin, end):
        l, r = begin, end
        if l >= r:
            return
        while l < r:
            while l < r and array[r] >= array[begin]: # 注意：如果选择最右边元素为pivot，
                r -= 1                                # 则下面两个while换位置
            while l < r and array[l] <= array[begin]:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = array[begin], array[l]
        recursive(begin, l-1)
        recursive(r+1, end)
    recursive(0, len(array)-1)
    return array
 

test = [-1, 1, 0, 5, 1, 4, 3, 4, 7, 5]
quick_sort(test, 0, len(test)-1)
print(test)
print(Solution2().findKthLargest([2, 1], 1))          
                