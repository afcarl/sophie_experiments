import string
import random

def generate_word(length=5, is_start_of_sentence=False):
    word = ''
    if is_start_of_sentence:
        word += random.choice(string.ascii_uppercase)
        length -= 1
    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word


def generate_sentence(num_words=10):
    sentence = ''
    for i in range(num_words):
        if i == 0:
            sentence += generate_word(length=random.randint(3,10), is_start_of_sentence=True) + ' '
        if i < (num_words - 1):
            sentence += generate_word(length=random.randint(3,10)) + ' '
        else:
            sentence += generate_word(length=random.randint(3,10)) + '.'
    return sentence


def generate_paragraph(num_sentences=5):
    paragraph = ''
    for i in range(num_sentences):
        paragraph += generate_sentence(num_words=random.randint(7, 15))
    return paragraph
