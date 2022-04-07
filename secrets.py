'''Check secret'''
import re

import sys

files = sys.argv[1:]


REGEXP =r'[a-zA-Z0-9_\-]*KEY[(\W?)*]=[(\W?)*][a-zA-Z0-9_\-]*'

secrets = []

for file in files:
    if sys.argv[0] not in file:

        with open(file, encoding='utf-8') as f:
            for lineno, line in enumerate(f.readlines()):
                if re.search(REGEXP, line):
                    secrets.append((line, lineno, file))


if len(secrets) > 0:
    print('secrets: ')
    for secret in secrets:
        print(f'line {secret[1]} in {secret[2]}:\t{secret[0]}')

else:
    print('No secrets in .py files')
