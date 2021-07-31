import unittest

def merge_ranges(time_range):
   
    sorted_times = sorted(time_range)
    
    merged_meetings = [sorted_times[0]]
    
    for current_meeting_start, current_meeting_end in sorted_times[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, 
                                    max(last_merged_meeting_end, 
                                        current_meeting_end))

        else: 
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

    
# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_no_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (4, 6)])
        expected = [(1, 3), (4, 6)]
        self.assertEqual(actual, expected)
    
    def test_all_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (3, 7), (5, 10)])
        expected = [(1, 10)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(1, 3), (3, 5)])
        expected = [(1, 5)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(3, 5), (4, 6), (1, 2)])
        expected = [(1, 2), (3, 6)]
        self.assertEqual(actual, expected)

    def test_contains_other_meetings(self):
        actual = merge_ranges([(1, 8), (3, 4)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)