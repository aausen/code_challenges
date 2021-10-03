# merge meetings

def merge_meetings(meeting_times):
    # sort the meetings
    # new list of merged meetings starting with first meeting in sorted meetings
    # for current start, current end in sorted meetings - start at second meeitng
    # comapare current meeting to last meeting in merged meetings
    # if current start is less than last end:
    #   new meeting = min (current start, last start), max(current end, last end)
    # else add meeting to the end of the list
    # return list of merged meetings

    sorted_meetings = sorted(meeting_times)
    merged_meetings = [sorted_meetings[0]]

    for current_start, current_end in sorted_meetings[1:]:
        last_start, last_end = merged_meetings[-1]
        if current_start <= last_end:
            merged_meetings[-1] = (min(current_start, last_start),
                                    max(current_end, last_end))
        else:
            merged_meetings.append((current_start, current_end))

    return merged_meetings

# reverse list in place
def reverse_in_place(char_list):
    # left index and right index
    # while left index less than right index
    # left index, right index = right index, left index

    left_index = char_list[0]
    right_index = len(char_list) - 1

    while left_index < right_index:
        char_list[left_index], char_list[right_index] = char_list[right_index], char_list[left_index]
        left_index += 1
        right_index -= 1

# reverse words
def reverse_words(message):
    reverse_characters(message, 0, len(message)-1)

    current_word_start_index = 0

    for i in range(len(message)+1):
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i-1)
            current_word_start_index += 1

def reverse_characters(message, left_index, right_index):
    while left_index < right_index:
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]

        left_index += 1
        right_index -= 1