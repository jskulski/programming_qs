# given a matrix of words and a dictionary
# [
#  [ 'c, 'a', 't', 'e'  ]
#  [ 'a', 'r', 't', 's' ]
#  [ 'r', 'e', 'n', 't' ]
# ]
#
# find all words: horizontal, veritcal and diagonal
#
# e.g. cat, ate, at, a, car, are, est, rent, arts, art

def find_words_in_matrix():
    # lets compose first
    pass

words = set()
def find_word_in_list(letters, dictionary, words=set()):
    if not letters:
        return words
    words = words.union(get_words_forward(dictionary, letters))
    words = words.union(get_words_backwards(dictionary, letters))
    return words.union(
        find_word_in_list(letters[1:], dictionary, words),
        find_word_in_list(letters[:-1], dictionary, words)
    )


def get_words_backwards(dictionary, letters):
    words = set()
    possible_list = letters
    while letters:
        possible_word = "".join(letters)
        if is_list_a_word(dictionary, possible_word):
            words.add(possible_word)

        letters = letters[1:]

    return words


def get_words_forward(dictionary, letters):
    words = set()
    possible_word = ''
    for letter in letters:
        possible_word += letter
        if is_list_a_word(dictionary, possible_word):
            words.add(possible_word)
    return words


def is_list_a_word(dictionary, possible_word):
    return possible_word in dictionary


def test(actual, expected):
    try:
        assert expected == actual
        print 'PASS!'
    except Exception:
        print 'FAIL!'
        print 'expected %s to equal %s' % (actual, expected)


def rotate(matrix):
    print [ i for i in len(matrix[0]) ]
    return matrix




# Test finding a word in ['d','o','g']
word_set = {'a',
             'do',
             'dog',
             'ogre',
             'cat',
             'ate',
             'at'}

test(find_word_in_list(['a'], word_set), {'a'})
test(find_word_in_list(['d'], word_set), set())

test(find_word_in_list(['d', 'o'], word_set), {'do'})

test(find_word_in_list(['d', 'o', 'g'], word_set), {'do', 'dog'})

test(
    find_word_in_list(['d', 'o', 'g', 'r', 'e'], word_set),
    {'do',
     'dog',
     'ogre'}
)

# cate
test(
    find_word_in_list(['c', 'a', 't', 'e'], word_set),
    {'cat', 'at', 'ate', 'a'}
)

# # Test transpose
# test(rotate([[1]]), [[1]])
# test(rotate([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

