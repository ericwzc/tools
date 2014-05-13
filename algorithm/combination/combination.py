__author__ = 'erwang'

def getcombin(n, r, tracker = []):
    while n >= r:
        tracker.append(n)
        if r > 1:
            getcombin(n-1, r -1, tracker)
        else:
            print(tracker)
        tracker.pop()
        n -= 1

getcombin(4, 3);



