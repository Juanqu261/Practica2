from estructuras import DoubleList, Stack, Queue


def middle(d_list, start, end):
    """
    [Summary]:
        Devuelve el nodo medio de una lista doblemente enlazada dada su nodo de inicio y finalización.

    [Args]:
    d_list(DoubleList): lista doblemdente enlazada.
    start(DoubleNode): el nodo de inicio de la sublista a considerar.
    end(DoubleNode): el nodo final de la sublista a considerar.

    [Returns]:
    - El nodo que buscado o None si no existe lo que se busca
    """

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


def lista_pila(list:DoubleList):
    stack = Stack()
    temp = list.get_last()
    for i in range(list.size):
        stack.push(temp)
        temp = temp.get_prev()
    return stack

def lista_cola(list:DoubleList):
    queue = Queue()
    temp = list.get_last()
    for i in range(list.size):
        queue.enqueue(temp)
        temp = temp.get_prev()
    return queue