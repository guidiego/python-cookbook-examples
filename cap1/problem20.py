from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)

print('< x >', c['x'])
print('< y > ', c['y'])
print('< z >: ', c['z'])

print('< Length >', len(c))
print('< Keys >', list(c.keys()))
print('< Values >', list(c.values()))

c['z'] = 10
print('New A', a)
