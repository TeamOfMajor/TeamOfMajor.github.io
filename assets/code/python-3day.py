# -*- coding: utf-8 -*-

# 1
print (type('가'))
print('가'.encode('utf-8'))
print(type('가'.encode('utf-8')))
# 2
print(ord('s'))
print(chr(115))
# 3
colors = ['red', 'green', 'gold']
print(colors)
print(type(colors))
colors.append('blue')
print(colors)
colors.insert(1, 'black')
print(colors)
colors.extend(['white', 'gray'])
print(colors)
colors += ['red']
print(colors)
colors += 'red'
print(colors)
print(colors.index('red'))
print(colors.index('red', 1))
#print(colors.index('red'1, 5))
print(colors.count('red'))
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)