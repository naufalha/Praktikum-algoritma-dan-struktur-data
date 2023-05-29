import re
file = open("indonesia.txt", "r", encoding = 'latin1')
teks = file.read()
file.close()
d = r"di\w+"
array = []
string = re.findall(d, teks)
for i in range(0,len(string)):
   # print(string[i])
   if len(string[i]) > 3 and string[i] not in array :
         array.append(string[i])
string.clear()
print(array)