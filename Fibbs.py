def fibs(n):

    if n < 1:

        return 0

    if n == 1 or n == 2:

        return 1

    curr, prev = 1 , 1

    total = 0

    for i in range(3,n+1):

        total = curr + prev

        prev = curr

        curr = total

    return total


print(fibs(20))
