import random
import string
from wordlist import get_words


def main():
    get_random_string(16)
    generate_password_from_words()


def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(length))
    print("Random string is", result_str)


def generate_password_from_words():
    words = get_words()
    word_list = []
    for i in range(4):
        rand_word = random.choice(words)
        word_list.append(rand_word)

    print("Password: ", word_list)


if __name__ == '__main__':
    main()
