#
# Given a list of denominations and a total, return the smallest number of coins
# that will add up to that total
#
# hint. Assume sorted largest to smallest
#

def determine_coins(target, denominations):
    left = target
    coins = []

    while (left > 0):
        for denomination in denominations:
            if left >= denomination:
                chosen = denomination
                coins.append(chosen)
                left -= chosen

    return coins


def find_shortest(target, denominations):
    possibilities = []
    while denominations:
        possibilities.append(determine_coins(target, denominations))
        denominations = denominations[1:]

    shortest_possibility = None
    for possibility in possibilities:
        if not shortest_possibility or len(possibility) < len(shortest_possibility):
            shortest_possibility = possibility

    print shortest_possibility


def test(target, denominations, expected):
    result = determine_coins(target, denominations)

    print "checking if coins(%s, %s) is %s" % (target, denominations, expected)
    print "result of coins(%s,%s) is %s" % (target, denominations, result)

    if expected == result:
        print 'PASS!'
    else:
        print 'FAIL!!!'
        # assert False



test(1, [1], [1])
test(2, [1], [1, 1])
test(3, [1], [1, 1, 1])

test(1, [5, 1], [1])
test(5, [5, 1], [5])

test(6, [5, 1], [5, 1])

test(10, [8, 7, 2, 1], [8, 2])

test(8, [6, 5, 3, 1], [5, 3])

find_shortest(8, [6, 5, 3, 1])
