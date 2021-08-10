class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        current_word_start_index = 0
        current_word_length = 0
        
        for i, char in enumerate(input_string):
            if i == len(input_string) - 1:
                if char.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index: 
                        current_word_start_index + current_word_length]
                    self.add_word_to_dict(current_word)

            elif char == " " or char == "\u2014":
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index: 
                        current_word_start_index + current_word_length]
                    self.add_word_to_dict(current_word)
                    current_word_length = 0

            elif char == ".":
                if i < len(input_string) - 1 and input_string[i + 1] ==".":
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dict(current_word)
                        current_word_length = 0

            elif char.isalpha() or char == "\'":
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            elif char == "-":
                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dict(current_word)
                        current_word_length = 0

    def add_word_to_dict(self, word):
        if word in self.words_to_counts:
            self.words_to_counts += 1

        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        else:
            self.words_to_counts[word] = 1