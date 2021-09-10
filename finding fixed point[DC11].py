

def DC_find(arr,l,r):

   #print(f"{l} , {r}")

   if l > r:

      return -1

   pos = int((l+r)/2)

   val = pos + 1

   if val == arr[pos] :

      return val

   if val > arr[pos]:

      return DC_find(arr,pos+1,r)

   else:

      return DC_find(arr,l,pos-1) #------------------ (1)


def finding_fixed_point(arr):

   
   return DC_find(arr,0,len(arr))


if __name__ == "__main__":

   sorted_array = [-3,0,1,4,12,17,20,22]

   idx_true = finding_fixed_point(sorted_array)

   sorted_array = [ -3,0,1,7,12,17,20,22]

   idx_false = finding_fixed_point(sorted_array)
