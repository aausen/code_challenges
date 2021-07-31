def merge_ranges(time_range):
    # sort the list by start times
    print("times: ", time_range)
    sorted_times = sorted(time_range)
    print("sorted", sorted_times)
    # first = meeting with earlier start time
    # second = meeting with later start time
    # if the end time of the first meeting is
    #   greater thank or equal to the start time of the 
    #   second meeting, merge the two meetings
    #   the result will be the first meeting's start time
    #   and the end time will be the later of the two meeting's end times
    # else we leave them seperate
    # return a merged list of times


merge_ranges([(1,3), (2, 4), (7, 9), (3, 10)])