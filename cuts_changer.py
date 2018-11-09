import argparse
import random

parser = argparse.ArgumentParser(description='A script which replaces string cuts')

parser.add_argument('--random', help='1 for random russian words, 0 for your choice', required=True)
parser.add_argument('--input', default='input.txt', help='Input file name')
parser.add_argument('--output', default='output.txt', help='Output file name')
parser.add_argument('--old_cut', default=',', help='A string to be replaced')
parser.add_argument('--new_cut', default=', блять,', help='A string which will replace the old')

args = vars(parser.parse_args())

words = (
    'блять', 'бля', 'пиздецово', 'сука', 'пизда', 'ебануто', 'нихуя',
    'мудаковато', 'еблан', 'залупа', 'ебануто', 'хуёво', 'херово'
)
last_word = ''
one_more_word = ''

with open(args['input'], 'r', encoding='UTF-8') as f:
    string = f.read()

    if not int(args['random']):
        string = string.replace(args['old_cut'], args['new_cut'])
    else:
        b = 0

        while True:
            try:
                a = string.index(args['old_cut'], b)
            except ValueError:
                break

            while True:
                word = random.choice(words)
                if word != last_word:
                    last_word = word
                    break

            if random.randint(1, 5) == 5:
                while True:
                    one_more_word = random.choice(words)
                    if one_more_word != word:
                        word = ' '.join((word, one_more_word))
                        break

            if word.endswith(('блять', 'бля', 'еблан', 'залупа', 'пизда', 'сука')):
                word = word + ','

            b = a + len(word) + 2

            string = string[:a + 1] + ' ' + word + string[a + 1:]
            print('Adding word:', word)

with open(args['output'], 'w', encoding='UTF-8') as f:
    f.write(string)
    print('Done!')
