import re
f = open('indonesia.txt', 'r')
teks = f.read()
f.close()
cocok = r'me\w+'
print(cocok)