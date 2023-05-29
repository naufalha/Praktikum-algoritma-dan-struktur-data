import re
f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
f.close()
pola = r'([\w+]+)</a></td>'
tampil = re.findall(pola, teks)

f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
string = re.findall(r'title="([\w+]+)">',teks)

string = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
list = []
for i in string:
    list.append((i[0], float(i[1])))


print(list)
