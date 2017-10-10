def add(self,item):
    temp = Node(item)
    temp.next = self.head
    self.head = temp
    current = self.head
    while current.position != self.size - 1:
        previous=current
        current=current.next
        current.back=previous


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
            midpoint = (first + last)//2
        if alist[midpoint] == item:
                found = True
        else:
            if item < alist[midpoint]:
                    last = midpoint-1
            else:
                first = midpoint+1
    return found
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]



