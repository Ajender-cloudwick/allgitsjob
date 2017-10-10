# function to find the once appearing element in array


def quicksortcall(alist,st,end):
    if st < end:
        part = quicksort(alist,st,end)
        quicksortcall(alist,st,part-1)
        quicksortcall(alist,part+1,end)


def quicksort(alist,st,end):
    piv = alist[st]
    first = st + 1
    last = end
    done = False
    while not done:

        while alist[first] <= piv and first <= last:
            first = first + 1
        while alist[last] >= piv and first <= last:
            last = last - 1
        if first > last:
            done = True
        else:
            temp = alist[first]
            alist[first] = alist[last]
            alist[last]=temp
    tmp = alist[last]
    alist[last] =  alist[st]
    alist[st] = tmp
    return last


def dictcount():
    mylist = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    mydict = {}
    for i in mylist:
        if i in mydict: mydict[i] += 1
        else: mydict[i] = 1
    print mydict
dictcount()
