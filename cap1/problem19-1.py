from collections import ChainMap


values = ChainMap()
values['x'] = 1

# Adiciona um novo mapeamento
values = values.new_child()
values['x'] = 2

# Adiciona um novo mapeamento
values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])

# Descarta o último mapeamento
values = values.parents
print(values['x'])

# Descarta o último mapeamento
values = values.parents
print(values['x'])

print(values)
