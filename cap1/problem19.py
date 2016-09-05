import os

nums = [1,2,3,4,5]
s = sum(x * x for x in nums)

print('SUM')
print(s)

files = os.listdir('./')

if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no py') 

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portifolio = [
    {'name': 'GOOG', 'shares': 50}, 
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portifolio)
print(min_shares)


