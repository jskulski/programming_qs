# Given an integer, and a list of integers, are there two integers in that list
# that add up directly to the first given integer


def choose_movies(flight_length, movies):
    """
    First attempt. Non pythonic because I don't know python that well :)
    :param flight_length:
    :param movies:
    :return:
    """
    choice = []

    for i, first_length in enumerate(movies):
        for j, second_length in enumerate(movies):

            if i == j:
                continue

            if first_length + second_length == flight_length:
                choice = [j, i]

    return choice

def choose_movies_pythonic(flight_length, movies_lengths):
    combined_lengths = [ ilen + jlen for i, ilen in enumerate(movies_lengths) for j, jlen in enumerate(movies_lengths) if j != i ]
    return flight_length in combined_lengths


def test(actual, expected):
    try:
        assert actual == expected
        print 'PASS!'
    except Exception:
        print 'FAIL!'
        print 'expected %s to equal expected %s' % (actual, expected)


# Test first version
test(choose_movies(10, [5, 5]), [0, 1])
test(choose_movies(10, [7, 7]), [])

test(choose_movies(10, [3, 5, 7]), [0, 2])
test(choose_movies(10, [5, 3, 7]), [1, 2])

test(choose_movies(10, [7, 2, 1, 3]), [0, 3])
test(choose_movies(20, [1, 10, 10, 3]), [1, 2])

# Pythonic
test(choose_movies_pythonic(10, [5, 5]),  True)
test(choose_movies_pythonic(10, [7, 7]), False)

test(choose_movies_pythonic(10, [3, 5, 7]), True)
test(choose_movies_pythonic(10, [5, 3, 7]), True)

test(choose_movies_pythonic(10, [7, 2, 1, 3]), True)
test(choose_movies_pythonic(20, [1, 10, 10, 3]), True)

