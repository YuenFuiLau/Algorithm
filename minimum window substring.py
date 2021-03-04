def mini_win_substring(s,t):

    need = {}
    window = {}

    N = len(s)

    for i in t:

        if i in need:

            need[i] += 1

        else:

            need[i] = 1

    iter_list = list(s)

    left,right = 0, 0

    start = 0
    mini_len = N + 1

    flag = 0

    while right < N:

        k1 = iter_list[right]
        right += 1

        if k1 in need:

            if k1 in window:

                window[k1] += 1

            else:

                window[k1] = 1

            if window[k1] == need[k1]:

                flag += 1

        while flag == len(need):

            if (right - left) < mini_len:

                start = left
                mini_len = right - left

            k2 = iter_list[left]

            left += 1

            if k2 in need:

                if window[k2] == need[k2]:

                    flag -= 1

                window[k2] -= 1


    if mini_len == N+1:

        return ""

    return "".join(iter_list[start:start+mini_len])
            



s = "ADOBECODEBANC"
t = "ABC"


ans = mini_win_substring(s,t)



s = "ADOBECFHKHSUYWYORHGBCNBZMNZHJIUWXHHROWIXJWQXNCNJSLOIPKJHKHFBANC"
t = "XSR"


ans = mini_win_substring(s,t)
