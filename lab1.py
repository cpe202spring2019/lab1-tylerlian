
def max_list_iter(int_list):  # must use iteration not recursion
   maximum = int_list[0]
   for i in range(1,int_list):
      if int_list[i] > maximum:
         maximum = int_list[i]
   return maximum

def reverse_rec(int_list):   # must use recursion
   if len(int_list) == 0:
      raise ValueError
   elif int_list[0] > int_list[1]:
      
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
