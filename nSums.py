def sums2(nums,target):
    
    m = len(nums)
    hi = m - 1
    lo = 0
    
    ans = []
    
    while lo < hi :
        
        left = nums[lo]
        right = nums[hi]
        
        tmp = left + right
        
        if tmp == target:
            
            ans.append([left,right])
            
            while lo<hi and nums[lo] == left: lo += 1
            while lo<hi and nums[hi] == right: hi -= 1
                
        elif tmp < target:
            
            while lo<hi and nums[lo] == left: lo += 1
                
        elif tmp > target:
            
            while lo<hi and nums[hi] == right: hi -= 1
                
    return ans

def nSums(nums,target,n):

    m = len(nums)
    
    if n < 2 or n > m:
        
        return []
    
    if n == 2:
        
        return sums2(nums,target)

    
    ans = []
    
    i = 0
    
    while i < m:
        
        curr_nums = nums[i]
        
        tmp = nSums(nums[i+1:],target-curr_nums,n-1)
        
        for data in tmp:
            
            data.append(curr_nums)
            ans.append(data)
            
        while i<m and curr_nums == nums[i]: i += 1
            
    return ans


nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()

ans = nSums(nums,target,4)



