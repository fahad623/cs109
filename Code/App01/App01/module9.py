from operator import itemgetter

data = [(1,7,3), (4,5,6), (7,8,9), (2,2,2)]

data.sort(key=itemgetter(1))

print data[-2:]