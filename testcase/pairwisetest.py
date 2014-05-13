__author__ = 'erwang'

import itertools
import sys


def dumpall(lst):
    for i in lst:
        print(i)


def nicePrint(lst):
    for item in lst:
        print("{0:<20}".format(item), end='')
    print()


def getallpairs(allvars):
    tmp = []
    for key in sorted(allvars.keys()):
        tmpitem = [key]
        tmpitem.extend(allvars[key])
        tmp.append(tmpitem)
    allvars = tmp
    pairs = []
    while len(allvars) > 1:
        for i in allvars[1:]:
            grp = []
            for j in allvars[0][1:]:
                for k in i[1:]:
                    grp.append((allvars[0][0], i[0], j, k))
            pairs.append(grp)
        allvars = allvars[1:]
    return pairs


def tuplegenerator(lst):
    size = len(lst)
    while size:
        ps = itertools.combinations(lst, size)
        for p in ps:
            yield p
        size -= 1


def getcase(pairs, covered, cats):
    filtered = []
    for grp in pairs:
        tmp = [i for i in grp if (lambda x: x not in covered)(i)]
        if tmp:
            filtered.append(tmp)
    history = []
    memo = {'Continue': True}
    workpairs = tuplegenerator(filtered)
    for workpair in workpairs:
        # print(workpair)
        getbestcase(pairs, workpair, history, cats, covered, memo)
        if not memo['Continue']:
            break
    ls = list(memo.keys())
    ls.remove('Continue')
    best = memo[max(ls)]
    case = gencase(best, covered)
    nicePrint(case)
    return case


def gencase(pairs, covered):
    catval = {}
    for pair in pairs:
        covered[pair] = True
        catval[pair[0]] = pair[2]
        catval[pair[1]] = pair[3]
    return [catval[key] for key in sorted(catval.keys())]


def getbestcase(unfiltered, filtered, history, cats, covered, memo):
    if len(history) == len(filtered):
        fixempty(history, unfiltered, cats)
        counter = countuncoveredpairs(history, covered)
        if counter == len(filtered):
            memo[counter] = history[:]
            memo['Continue'] = False
        elif counter not in memo:
            memo[counter] = history[:]
        return
    idx = len(history)
    for pair in filtered[idx]:
        history.append(pair)
        if not isvalid(history):
            history.pop()
            continue
        getbestcase(unfiltered, filtered, history, cats, covered, memo)
        if not memo['Continue']:
            break
        history.pop()


def fixempty(pairs, unfiltered, cats):
    memo = {}
    for pair in pairs:
        if pair:
            memo[pair[0]] = pair[2]
            memo[pair[1]] = pair[3]

    missing = set(cats).difference(set(memo.keys()))
    if missing:
        coms = []
        if len(missing) > 1:
            coms.extend(itertools.combinations(missing, 2))
        for i in missing:
            for j in memo.keys():
                coms.append((i, j))
        pairs.extend(foundinorigin(coms, memo, unfiltered))


def foundinorigin(coms, memo, unfiltered):
    result = []
    for i in coms:
        missings = foundmatchinorigin(sorted(i), unfiltered)
        for j in missings:
            if j[0] in memo and j[2] != memo[j[0]]:
                continue
            if j[1] in memo and j[3] != memo[j[1]]:
                continue
            # either one is in, or both not in
            result.append(j)
            memo[0] = j[2]
            memo[1] = j[3]
            break
    return result


def foundmatchinorigin(tup, unfiltered):
    for i in unfiltered:
        first = list(i[0][:2])
        if first == tup:
            return i
    return []


def isvalid(pairs):
    memo = {}
    for pair in pairs:
        if not validate(pair, 0, 2, memo) or not validate(pair, 1, 3, memo):
            return False
    return True


def validate(pair, nmidx, validx, memo):
    if pair[nmidx] not in memo:
        memo[pair[nmidx]] = pair[validx]
    else:
        if memo[pair[nmidx]] != pair[validx]:
            return False
    return True


def countuncoveredpairs(choices, covered):
    counter = 0
    for choice in choices:
        if choice not in covered:
            counter += 1
    return counter


def markpairs(case, covered):
    while len(case) > 1:
        for i in case[1:]:
            covered[case[0], i] = True
        case = case[1:]


def gettestcases(allvars):
    pairs = getallpairs(allvars)
    # dumpall(pairs)
    pairnum = sum([len(i) for i in pairs])
    cases = []
    covered = {}
    nicePrint(allvars.keys())
    while len(covered) < pairnum:
        case = getcase(pairs, covered, allvars.keys())
        cases.append(case)
    return cases


def getinput(absfilepath):
    myvars = {}
    with open(absfilepath, 'r') as f:
        for line in f.readlines():
            if line:
                tmp = line.split(':')
                myvars[tmp[0].strip()] = [i.strip() for i in tmp[1].split(',')]

    return myvars

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: pyhon pairwisetest.py inputfile")
        exit(1)
    file = sys.argv[1]
    myvars = getinput(file)
    print(myvars)
    gettestcases(myvars)


