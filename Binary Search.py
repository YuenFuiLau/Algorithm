class Solution(object):
    
    def right_bound(self,nums,target,N):
        
        left = 0 
        right = N - 1
        
        while(left <= right):
            
            mid = (left+right)//2
        
            if nums[mid] == target:
                
                left = mid + 1
                
            elif nums[mid] < target:
                
                left = mid + 1
                
            elif nums[mid] > target:
                
                right = mid - 1
                
        if right < 0 or nums[right] != target:
            
            return -1
        
        return right
    
    def left_bound(self,nums,target,N):
        
        left = 0
        right = N - 1
        
        while(left <= right):
            
            mid = (left+right)//2
            
            if nums[mid] == target:
                
                right = mid - 1
                
            elif nums[mid] < target:
                
                left = mid + 1
                
            elif nums[mid] > target:
                
                right = mid - 1
                
        if left >= N or nums[left] != target:
            
            return -1
        
        return left
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        
        if length == 0:
            
            return [-1,-1]
        
        return [self.left_bound(nums,target,length),self.right_bound(nums,target,length)]
