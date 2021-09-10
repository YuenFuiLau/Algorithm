def count(nums,target,l,r):

   count = 0

   for i in range(l,r):

      if nums[i] == target:

         count = count + 1


   if count > int((r-l+1)/2):
   
      return count

   else:

      return -1


def DC12(nums,l,r):

   if l==r:

      return nums[l]

   mid = int((l+r)/2)

   left = DC12(nums,l,mid)
   right = DC12(nums,mid+1,r)

   if left == right:

      return left

   left_nums = count(nums,left,l,mid+1)
   right_nums = count(nums,right,mid+1,r)
  
   if left_nums == -1 and right_nums == -1:

      return  -1
   
   if left_nums >right_nums:

      return left

   else:

      return right



def majorityElement( nums):
  
  return DC12(nums,0,len(nums)-1)


if __name__ == "__main__":

   nums = [6,6,9,9,8,8,3,3,2,2,1,1,6,6,6,6,6,6,6,6,6,6,6,6]

   res = majorityElement(nums)
