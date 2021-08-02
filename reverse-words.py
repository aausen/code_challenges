message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

def reverse_words(message):
    # reverse all the characters
    left_index = 0
    right_index = len(message) -1

    while left_index < right_index:
        message[left_index], message[right_index] = message[right_index], message[left_index]

        left_index += 1
        right_index -= 1

reverse_words(message)