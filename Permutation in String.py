def PIS(s,t):

    need = {}
    window = {}
    
    for i in t:

        if i in need:

            need[i] += 1

        else:

            need[i] = 1

    left,right = 0,0

    flag = 0

    s_list = list(s)

    N = len(s)

    while right < N:

        k1 = s_list[right]

        right += 1

        if k1 in need:

            if k1 in window:

                window[k1] += 1

            else:

                window[k1] = 1

            if window[k1] == need[k1]:

                flag += 1

        #print(s_list[left:right])

        while flag == len(need):

            #print(s_list[left:right],right-left,len(t))

            if (right-left)==len(t):

                return True

            k2 = s_list[left]

            left += 1

            if k2 in need:

                if window[k2] == need[k2]:

                    flag -= 1

                window[k2] -= 1



    return False


s = "eidboaooo"
t= "ab"

ans = PIS(s,t)

        
s = "eidbaooo"
t= "ab"

ans = PIS(s,t)
        
