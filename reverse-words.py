message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
def reverse_words(message):
    reverse_characters(message, 0, len(message)-1)

    current_word_start_index = 0

    for i in range(len(message) + 1):
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)

            current_word_start_index = i + 1

def reverse_characters(message, left_index, right_index):

    while left_index < right_index:
        message[left_index], message[right_index] = \
            message[right_index], message[left]

        left_index += 1
        right_index -= 1

# def reverse_words(message):
#     # reverse all the characters
#     left_index = 0
#     right_index = len(message) -1

#     while left_index < right_index:
#         message[left_index], message[right_index] = message[right_index], message[left_index]

#         left_index += 1
#         right_index -= 1

#     # This will reverse the whole message. The words will be the desired order, but the
#     # letters will be out of order
#     # need to find start and end indices of each word and do same thing

# reverse_words(message)