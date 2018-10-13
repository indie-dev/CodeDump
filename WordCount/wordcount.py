import sys, os

def get_word_count(text):
    split_text = text.split(" ")
    word_count = 0
    for split in split_text:
        word_count = word_count + 1
    return word_count

def main(argument):
    print("Word Count: " + str(get_word_count(argument)))

main(sys.argv[1])