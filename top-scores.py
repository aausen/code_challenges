import unittest

def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score+1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        for time in range(count):
            sorted_scores.append(score)

    return sorted_scores

class Test(unittest.TestCase):

    def test_no_score(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)
    
    def test_one_score(self):
        actual = sort_scores([5], 100)
        expected = [5]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([40, 70], 100)
        expected = [70, 40]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([55, 30, 77, 90, 20], 100)
        expected = [90, 77, 55, 30, 20]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([89, 45, 60, 60, 89, 45, 70], 100)
        expected = [89, 89, 70, 60, 60, 45, 45]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)