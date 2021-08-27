def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) -1
   

    while floor_index < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2

        guess_index = floor_index + half_distance

        guess_value = words[guess_index]

        if first_word > guess_value:
            ceiling_index = guess_index

        else:
            floor_index = guess_index

        if floor_index + 1 == ceiling_index:
            return ceiling_index
