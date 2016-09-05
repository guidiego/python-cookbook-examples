import re

line = 'asdf asd;alfre, michael, viado é    foo'

splited = re.split(r'[;,\s]\s*', line)

print('SPLITED STRING')
print(splited)

splited_for_remake = re.split(r'(;|,|\s)\s*', line)
print('SPLITED WITH DELIMITERS')
print(splited_for_remake)

values = splited_for_remake[::2]
print('ONLY VALUES')
print(values)

delimiters = splited_for_remake[1::2] + ['']
print('ONLY DELIMITERS')
print(delimiters)

line_again = ''.join(v+d for v,d in zip(values, delimiters))
print('LINE AGAIN MODAFCK')
print(line_again)
