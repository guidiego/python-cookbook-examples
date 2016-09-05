"""
    In OSX
    fnmatch('michael.txt', '*.TXT')
    >> FALSE

    In windows
    fnmatch('michael.txt', '*.TXT'))
    >> TRUE

    FOR THAT FUCKIN SHIT (WINDOW) OF SYSTEM YOU CAN USE FNMATCHCASE HUR DURRRRR
"""
from fnmatch import fnmatch, fnmatchcase

print('Everything endswith .txt', fnmatch('michael.txt', '*.txt'))

print('Start with F', fnmatch('foo.txt', '?oo.txt'))

print('Complex Regex', fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print('Filter with Generator', [name for name in names if fnmatch(name, 'Dat*.csv')])


#------------------------------------------------------------------------------------
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
