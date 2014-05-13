__author__ = 'erwang'

import itertools

def combgen(items):
    i = 1
    while i <= len(items):
        for j in itertools.combinations(items, i):
            yield j
        i += 1

def ones(lst):
    tmp = [i for i in lst if i == 1]
    return len(tmp)


def grpbyones(lst):
    memo = {}
    for i in lst:
        num = ones(i)
        if num not in memo:
            memo[num] = []
        memo[num].append(i)
    return [memo[i] for i in sorted(memo.keys())]


def combine(grps, unticked, combined={}, tomerge=[]):
    while len(grps):
        grp2 = []
        if len(grps) > 1:
            grp2 = grps[1]
        merge(grps[0], grp2, unticked, combined, tomerge)
        grps = grps[1:]

    # print(tomerge)

    if len(tomerge):
        combine(tomerge, unticked, combined, tomerge=[])


def merge(grp1, grp2, unticked, combined, tomerge):
    result = set()
    for i in grp1:
        counter = 0
        for j in grp2:
            merged = domerge(i,j)
            if merged:
                result.add(merged)
                combined[j] = 1
                counter += 1
        if not counter and i not in combined:
            unticked.append(i)
    if result:
        tomerge.append(list(result))

def domerge(i1, i2):
    diff_idx = -1
    diff_num = 0
    for i, v in enumerate(i1):
        if v != i2[i]:
            if not diff_num:
                diff_num += 1
                diff_idx = i
            else:
                return []
    if diff_idx == -1:
        return tuple(i1)
    result = list(i1[:])
    result[diff_idx] = '-'
    return tuple(result)

def minbool(candidates, exprs):
    coms = combgen(candidates)
    for com in coms:
       memo = {}
       for candidate in com:
            for expr in exprs:
                mark(candidate, expr, memo)
       if len(memo) == len(exprs):
            print(com)
            break;


def mark(candidate, expr, memo):
    for i in range(len(candidate)):
        if candidate[i] != expr[i]:
           if candidate[i] != '-':
               return
    memo[expr] = 1

exprs = [(0,0,0,0),
        (0,0,0,1),(0,0,1,0),(1,0,0,0),
        (0,0,1,1),(0,1,0,1),(1,0,1,0),(1,1,0,0),
        (0,1,1,1),(1,1,0,1),
        (1,1,1,1)
        ]

exprs = [
    (0,0,0,0),
    (1,0,0,0),
    (0,1,0,0),
    (1,0,1,0),
    (0,1,1,0),
    (1,1,1,0),
    (0,0,0,1),
    (1,0,0,1),
    (0,0,1,1),
    (1,0,1,1),
    (0,1,1,1),
    (1,1,1,1),
    ]

exprs = [(0,1,0), (1,0,1), (0,1,1), (1,1,0), (1,1,1)]

exprs = [(0,0,0,1),(0,0,1,0),(0,0,1,1),(0,1,1,1),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),(1,1,1,0),(1,1,1,1)]

unticked = []
combine(grpbyones(exprs),unticked)
# print(unticked)
minbool(unticked,exprs)

