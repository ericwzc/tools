__author__ = 'erwang'

import itertools

def convertinput(expr, memo, clean):
    result = []
    for ad in clean:
        result.extend(dobinarize(ad, memo.copy()))
    return list(set(result))


def dobinarize(ad, memo):
    negate= False
    for i in ad:
        if negate:
           memo[i] = '0';
           negate = False
           continue
        if i == '!':
           negate= True
        else:
           memo[i] = '1'

    keys = [ k for k in sorted(memo.keys()) if memo[k] == '*']

    tuples = []
    if keys:
       paddedTuple(memo, keys, tuples)
    else:
       tuples.append(tuple(memo[i] for i in sorted(memo.keys())))
    return tuples


def paddedTuple(eleMap, keys, tuples):
    if keys:
        for i in ['0', '1']:
            eleMap[keys[0]] = i
            paddedTuple(eleMap, keys[1:], tuples)
    else:
        tuples.append(tuple(eleMap[i] for i in sorted(eleMap.keys())))


def combgen(items):
    i = 1
    while i <= len(items):
        for j in itertools.combinations(items, i):
            yield j
        i += 1


def ones(lst):
    tmp = [i for i in lst if i == '1']
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
            return com

def mark(candidate, expr, memo):
    for i in range(len(candidate)):
        if candidate[i] != expr[i]:
           if candidate[i] != '-':
               return
    memo[expr] = 1


def simplify(expr):
    ands = expr.lower().split('+')
    memo = {}
    clean = []
    for ad in ands:
        trimmed = ad.strip()
        clean.append(trimmed)
        for i in trimmed:
            if i == '!':
                continue
            memo[i] = '*'
    converted = convertinput(expr, memo, clean)
    # print(converted)
    unticked = []
    combine(grpbyones(converted), unticked, {}, [])
    # print(unticked)
    minexpr = minbool(unticked, converted)
    # print(minexpr)
    keys = sorted(memo.keys())
    result_exprs = []
    for expr in minexpr:
        tmp = ''
        for k, v in enumerate(expr):
            if v != '-':
                if v == '0':
                    tmp += "!"
                tmp += keys[k]
        if tmp:
            result_exprs.append(tmp)
    if not result_exprs:
        result_exprs.append('true')
    return '+'.join(result_exprs)

