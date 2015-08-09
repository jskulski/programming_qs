#
# Given an integer, and a list of integers, are there two integers in that list
# that add up directly to the first given integer
#


def has_target_length(target_length, lengths):
    """
    First attempt. Non pythonic because I don't know python that well :)
    :param target_length:
    :param lengths:
    :return:
    """
    choice = []

    for i, first_length in enumerate(lengths):
        for j, second_length in enumerate(lengths):

            if i == j:
                continue

            if first_length + second_length == target_length:
                choice = [j, i]

    return choice

def has_target_length_pythonic(target_length, lengths):
    combined_lengths = [ ilen + jlen for i, ilen in enumerate(lengths) for j, jlen in enumerate(lengths) if j != i ]
    return target_length in combined_lengths


def test(actual, expected):
    try:
        assert actual == expected
        print 'PASS!'
    except Exception:
        print 'FAIL!'
        print 'expected %s to equal expected %s' % (actual, expected)


# Test first version
test(has_target_length(10, [5, 5]), [0, 1])
test(has_target_length(10, [7, 7]), [])

test(has_target_length(10, [3, 5, 7]), [0, 2])
test(has_target_length(10, [5, 3, 7]), [1, 2])

test(has_target_length(10, [7, 2, 1, 3]), [0, 3])
test(has_target_length(20, [1, 10, 10, 3]), [1, 2])

# Pythonic
test(has_target_length_pythonic(10, [5, 5]),  True)
test(has_target_length_pythonic(10, [7, 7]), False)

test(has_target_length_pythonic(10, [3, 5, 7]), True)
test(has_target_length_pythonic(10, [5, 3, 7]), True)

test(has_target_length_pythonic(10, [7, 2, 1, 3]), True)
test(has_target_length_pythonic(20, [1, 10, 10, 3]), True)

