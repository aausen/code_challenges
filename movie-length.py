import unittest
from unittest import result
def can_two_movies_fill_flight(flight_length, movie_lengths):
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie = flight_length - first_movie_length
        
        if matching_second_movie in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False


# Tests

class Test(unittest.TestCase):
    
    def test_short_flight(self):
        result = can_two_movies_fill_flight(1, [2, 3, 4])
        self.assertFalse(result)

    def test_long_light(self):
        result = can_two_movies_fill_flight(6, [2, 4])
        self.assertTrue(result)

    def test_one_move_half_flight_length(self):
        result = can_two_movies_fill_flight(6, [8, 2])
        self.assertFalse(result)

    def test_two_movies_half_of_flight(self):
        result = can_two_movies_fill_flight(6, [3, 8, 3])
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight(10, [4, 5, 3, 6, 2, 8])
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight(4, [4])
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight(5, [])
        self.assertFalse(result)

unittest.main(verbosity=2)