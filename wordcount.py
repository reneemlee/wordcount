"""Count words in file."""
import sys
import re


def word_count(filename):
    tokens = tokenize(filename)
    dict_of_words = count_words(tokens)
    print_word_counts(dict_of_words)

    # with open(filename) as file:

    #     word_count_dict = {}

    #     for line in file:       
    #         line = line.rstrip().split()

    #         for word in line:
    #             word_count_dict[word] = word_count_dict.get(word, 0) + 1

    #     return word_count_dict


def tokenize(filename):
    words = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip().split()
            words.extend(line)
    return words

def count_words(words):
    word_count_dict = {} 
    for word in words:
        word = word.lower()
        #removing spaces and punctuations from a string
        word = re.sub(r'[^\w\s]','',word)
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
    
    return word_count_dict

def print_word_counts(word_counts):
    for key, value in word_counts.items():
        print(f"{key} {value}")

# print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1})
word_count(sys.argv[1])