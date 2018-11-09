import argparse

parser = argparse.ArgumentParser(description='MY_DESC_1')
parser.add_argument('-f', '--foo', help='MY_ARG_DESC_1', required=True)
parser.add_argument('-b', '--bar', help='MY_ARG_DESC_2',required=False)

args = vars(parser.parse_args())

print('PRING_STATEMENT')
print(args)
print(123)
