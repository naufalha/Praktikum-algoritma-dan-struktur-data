import re
file = open("indonesia.txt", "r", encoding = 'latin1')
teks = file.read()
file.close()
tuple = ()
p = r"me\w+"
string = re.findall(p, teks)
for i in range(len(string)):
    if len(string[i]) > 3:
        tuple += (string[i],)
        
print(tuple)