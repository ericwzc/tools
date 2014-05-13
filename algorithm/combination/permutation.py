__author__ = 'erwang'


def lexp(lst1):
    print(lst1)
    while True:
        idx = findmin(lst1)
        if idx == -1:
            break;
        bigidx = findBig(lst1, idx)
        lst1[idx], lst1[bigidx] = lst1[bigidx], lst1[idx]
        temp = list(lst1[:idx + 1])
        temp.extend(reversed(lst1[idx + 1:]))
        lst1 = temp
        print(lst1)


def findmin(lst):
    if not lst:
        return -1
    n = len(lst) - 1
    while n:
        if lst[n - 1] < lst[n]:
            return n - 1
        n -= 1
    if n == 0:
        return -1


def findBig(lst1, idx):
    if idx == -1:
        return -1
    n = len(lst1) - 1
    while n > idx:
        if lst1[n] > lst1[idx]:
            return n
        n -= 1
    return -1


# lexp([1234])
lst = [1,2,3,4]
lst = []
# i = findmin(lst)
# print(i)
#
# j = findBig(lst,i)
# print(j)

lexp(lst)



