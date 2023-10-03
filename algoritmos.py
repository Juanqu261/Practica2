from estructuras import DoubleList


def middle(d_list, start, end):
    if start == None or end == None:
        return None
    if start == end:
        return start
    else:
        temp1 = d_list.get_head()
        temp2 = d_list.get_head()
        while temp2 != end:
            temp2 = temp2.get_next()
            if temp2 == temp2.get_next():
                temp2 = temp2.get_next()
                temp1 = temp1.get_next()
        return temp1


def binary_search(d_list, n):
    start = d_list.get_head()
    end = d_list.get_tail()
    mid = middle(d_list, start, end)
    while mid != None:
        if mid.get_data() == n:
            return mid
        elif mid < n:
            end = mid.get_prev()
        else:
            start = mid.get_next()
    mid = middle(d_list, start, end)
    return None
