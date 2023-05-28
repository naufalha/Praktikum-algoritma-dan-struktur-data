import re
file = open("indonesia.txt", "r", encoding = 'latin1')
teks = file.read()
file.close()
p = r"me\w+"
string = re.findall(p, teks)
print("No. 1")
print(string)