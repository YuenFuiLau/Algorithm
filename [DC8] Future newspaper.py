def DC8(stocks,l,r):

   if l == r:

      return 0
   
   mid =int((l+r)/2)
   
   res1 = DC8(stocks,l,mid)
   res2 = DC8(stocks,mid+1,r)

   min_p = min(stocks[l:mid+1])
   max_p = max(stocks[mid:r])

   return max(max_p-min_p,res1,res2)

if __name__ == "__main__":

   stocks = [1,5,6,8,9,112,6,5,48,6,2]

   res = DC8(stocks,0,len(stocks)-1)
