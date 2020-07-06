print('你好')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for key, value in favorite_languages.items():
    print('key=' + key)
    print('value=' + value)

for key in favorite_languages.keys():
    print('key=' + key)

for value in favorite_languages.values():
    print('value=' + value)

for value in favorite_languages:
    print('key=' + value)

for name in sorted(favorite_languages.keys()):
    print('name:'+name)