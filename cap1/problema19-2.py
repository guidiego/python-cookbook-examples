a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

c = {
    'x': 4,
    'u': 2
}

print('a: ', a)
print('b: ', b)
print('c: ', c)

print('Commons items (items in a in b)')
print(a.items() & b.items())
print('Common keys (keys in a in b)')
print(a.keys() & b.keys())
print('Intersection (keys in a not in b)')
print(a.keys() - b.keys())
print('Intersection (keys in b not in a)')
print(b.keys() - a.keys())
print('Intersection (items in a not in c)')
print(a.items() - c.items())
print('Intersection (keys in a not in c)')
print(a.keys() - c.keys())


# cria um novo dicionario com determindas chaves removidas
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print('Removing specific keys {\'z\', \'w\'} from a')
print(c)
