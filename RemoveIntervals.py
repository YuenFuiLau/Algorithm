
def removeCoveredIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    m =len(intervals)
    intervals.sort(key = lambda x:(x[0],-x[1]))
    left = intervals[0][0]
    right = intervals[0][1]

    
    ans = 0
    
    for intv in intervals[1:]:

        
        if left <= intv[0] and right >= intv[1]:
            
            ans += 1
            
        if right >= intv[0] and right < intv[1]:
            
            right = intv[1]
            
        if right < intv[0]:
            
            left = intv[0]
            right = intv[1]


            
    return (m-ans)


nums = [[1,2],[1,4],[3,4]]


ans = removeCoveredIntervals(nums)
