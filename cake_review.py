import unittest
import random

## Reverse string in place 8/16
def reverse(list_of_char):
    left_index = 0 
    right_index = len(list_of_char) - 1

    while left_index < right_index:
        list_of_char[left_index], list_of_char[right_index] = \
            list_of_char[right_index], list_of_char[left_index]

        left_index += 1
        right_index -= 1

# Tests for reverse

class Tests(unittest.TestCase):

    def test_even_list(self):
        list_of_char = ['a', 'b', 'c', 'd']
        reverse(list_of_char)
        expected = ['d', 'c', 'b', 'a']
        self.assertEqual(list_of_char, expected)

    def test_empty_list(self):
        list_of_char = []
        reverse(list_of_char)
        expected = []
        self.assertEqual(list_of_char, expected)

    def test_odd_list(self):
        list_of_char = ['a', 'b', 'c']
        reverse(list_of_char)
        expected = ['c', 'b', 'a']
        self.assertEqual(list_of_char, expected)
    
    def test_single_character(self):
        list_of_char = ['a']
        reverse(list_of_char)
        expected = ['a']
        self.assertEqual(list_of_char, expected)

## Can two movies fill the time of a flight 8/16
def can_two_movies_fill_flight(movie_lengths, flight_length):

    movie_lengths_seen = set()
    for current_movie in movie_lengths:
        second_movie = flight_length - current_movie
        if second_movie in movie_lengths_seen:
            return True
        movie_lengths_seen.add(current_movie)
    return False
can_two_movies_fill_flight([3, 4, 5], 7)

## apple stocks

def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('We need two prices to get a profit!')

    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]

    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        possible_profit = current_price - min_price

        max_profit = max(possible_profit, max_profit)

        min_price = min(current_price, min_price)
    
    return max_profit

## Highest Product of 3

def highest_product_of_three(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('There needs to be 3 numbers')

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_of_3 = max(highest_product_of_3,
                                    current * highest_product_of_2,
                                    current * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2, 
                                    current * highest,
                                    current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2, 
                                    current * highest,
                                    current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3

## Return merged arrays

def merge_lists(list1, list2):
    merged_list_size = len(list1 + list2)
    merged_list = [None] * merged_list_size
    current_idx_list1 = list1[0]
    current_idx_list2 = list2[0]
    current_idx_merged = merged_list[0]

    while current_idx_merged < merged_list_size:
        is_list1_exhausted = current_idx_list1 >= len(list1)
        is_list2_exhausted = current_idx_list2 >= len(list2)

        if (not is_list1_exhausted and 
                (is_list2_exhausted or 
                list1[current_idx_list1] < list2[current_idx_list2])):
            merged_list[current_idx_merged] = list1[current_idx_list1]
            current_idx_list1 += 1
        

        else: 
            merged_list[current_idx_merged] = list2[current_idx_list2]
            current_idx_list2 += 1
            
        current_idx_merged += 1

    return merged_list

## Merge meeting times

def merged_ranges(meeting_times):
    sorted_meetings = sorted(meeting_times)
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start_time, current_meeting_end_time in sorted_meetings:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start_time <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, 
                                    max(last_merged_meeting_end,
                                        current_meeting_end_time))
        else:
            merged_meetings.append((current_meeting_start_time, current_meeting_end_time))

    return merged_meetings

# Tests

class Test(unittest.TestCase):
    def test_two_meetings(self):
        meeting_times = [(1, 3), (2, 4)]
        result = merged_ranges(meeting_times)
        expected = [(1, 4)]
        self.assertEqual(result, expected)

    def test_no_overlap(self):
        meeting_times = [(1, 2), (4, 5)]
        result = merged_ranges(meeting_times)
        expected = [(1, 2), (4, 5)]
        self.assertEqual(result, expected)

    def test_end_and_start_same(self):
        meeting_times = [(1, 4), (4, 6)]
        result = merged_ranges(meeting_times)
        expected = [(1, 6)]
        self.assertEqual(result, expected)

    def test_many_meetings(self):
        meeting_times = [(1, 3), (4, 6), (5, 7), (7, 8)]
        result = merged_ranges(meeting_times)
        expected = [(1, 3), (4, 8)]
        self.assertEqual(result, expected)

    def test_meetings_out_of_order(self):
        meeting_times = [(3, 5), (1, 4), (8, 9), (3, 8)]
        result = merged_ranges(meeting_times)
        expected = [(1, 9)]
        self.assertEqual(result, expected)

# shuffle in place 

def get_random(floor, ceiling):
    return randrange(floor, ceiling + 1)

def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    for index_we_are_choosing_for in range(0, len(the_list) - 1):
        random_choice_index = get_random(index_we_are_choosing_for, last_index_in_the_list)

        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing_for]


['duck', 'cat', 'dog', 'fish']

# find rotation point
def find_rotation_point(words):

    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        if words[guess_index] >= first_word:
            floor_index = guess_index

        else:
            ceiling_index = guess_index

        if floor_index + 1 == ceiling_index:
            return ceiling_index

# merge meetings HiCal

def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for current_meeting in sorted_meetings[1:]:
        start_current, end_current = current_meeting
        start_last, end_last = merged_meetings[-1]

        if (start_current <= end_last):
            merged_meetings[-1] = (start_last, 
                                    max(end_current, end_last))
        else:
            merged_meetings.append((start_current, end_current))

    return merged_meetings

# top scores

def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in range(len(score_counts) -1, -1, -1):
        count = score_counts[score]

        for time in range(count):
            sort_scores.append(score)

    return sorted_scores

unittest.main(verbosity=2)