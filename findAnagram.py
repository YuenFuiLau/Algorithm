def findAnagrams(s, p):
  
    ans =[]
    need = {}
    window = {}
    
    for i in p:
        
        if i in need:
            
            need[i] += 1
            
        else:
            
            need[i] = 1
            
    s_list = list(s)
    
    left,right = 0,0
    
    flag = 0
    
    N = len(s)
    
    while right<N:
        
        k1 = s_list[right]
        
        right += 1
        
        if k1 in need:
            
            if k1 in window:
                
                window[k1] += 1
                
            else:
                
                window[k1] = 1
                
            if window[k1] == need[k1]:
                
                flag += 1
                
        while (right-left)==len(p):
            
            if flag == len(need):
                
                ans.append(left)
                
            k2 = s_list[left]
            left += 1
            
            if k2 in need:
                
                if window[k2] == need[k2]:
                    
                    flag -= 1
                    
                window[k2] -= 1
                
                
    return ans

s = "cbaebabacd"
p = "abc"

ans = findAnagrams(s,p)
