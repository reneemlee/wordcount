"""Count words in file."""
#function, take in filename
def word_count(filename):
    with open(filename) as file:

        word_count_dict = {}

        for line in file:       
            line = line.rstrip().split()

            for word in line:
                word_count_dict[word] = word_count_dict.get(word, 0) + 1

        return word_count_dict


print(word_count("test.txt"))
