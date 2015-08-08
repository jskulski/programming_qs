# https://www.interviewcake.com/question/inflight-entertainment


def choose_movies(flight_length, movies):
    choice = []

    for i, first_length in enumerate(movies):
        for j, second_length in enumerate(movies):

            if i == j:
                continue

            if first_length + second_length == flight_length:
                choice = [j, i]

    return choice

def test(actual, expected):
    try:
        assert actual == expected
        print 'PASS!'
    except Exception:
        print 'FAIL!'
        print 'expected %s to equal expected %s' % (actual, expected)




test(choose_movies(10, [5, 5]), [0, 1])
test(choose_movies(10, [7, 7]), [])

test(choose_movies(10, [3, 5, 7]), [0, 2])
test(choose_movies(10, [5, 3, 7]), [1, 2])

test(choose_movies(10, [7, 2, 1, 3]), [0, 3])

test(choose_movies(20, [1, 10, 10, 3]), [1, 2])
