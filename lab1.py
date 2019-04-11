
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
       raise ValueError
    if int_list == []:
       return None
    maximum = int_list[0]
    for i in range(1,len(int_list)):
        if int_list[i] > maximum:
            maximum = int_list[i]
    return maximum

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError  
    if len(int_list) <= 1:
        return int_list
    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    if low <= high:
        average = (low+high)//2
        if target == int_list[average]:
            return average
        elif target > int_list[average]:
            return bin_search(target,average+1,high,int_list)
        else:
            return bin_search(target,low,average-1,int_list)
    return None
