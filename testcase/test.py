__author__ = 'erwang'

# import itertools


myvars = [[1, 2, 11], [3, 4, 9], [5, 8, 6]]


def getallcoms(allvar):
    if len(allvar) == 1:
        return [[x] for x in allvar[0]]
    result = []
    for i in getallcoms(allvar[1:]):
        for j in allvar[0]:
            ele = [j]
            ele.extend(i)
            result.append(ele)
    return result

coms = getallcoms(myvars)

# print(len(result));


def getallpairs(item):
    pair = []
    while len(item) > 1:
        pair.extend([(item[0], i) for i in item[1:]])
        item = item[1:]
    return pair


def test(allitems):
    s = set()
    for item in allitems:
        k = getallpairs(item)
        for i in k:
            s.add(i)
    return len(s) == 27

# ft = itertools.combinations(coms, 9)
# print(getAllPairs([1,3,5,7]))
# for items in ft:
#     if test(items):
#         print('found:')
#         print(items)
#         break
#     print(items)

for pr in getallpairs([1, 2, 3, 4]):
    print(pr)
