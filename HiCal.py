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
    
    


merge_ranges([(1,3), (2, 4), (7, 9), (3, 10)])