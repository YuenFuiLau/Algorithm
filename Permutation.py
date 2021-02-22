
res =[]

def permute(nums,path=[]):

    if len(path) == len(nums):

        res.append(path)

        return


    for i in nums:

        if i in path:

            continue

        path.append(i)

        permute(nums,path[:])

        path.pop()


    return res



ans = permute([1,2,3,4,5,6,7,8,9])
