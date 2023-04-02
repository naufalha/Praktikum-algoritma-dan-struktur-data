def SoLong(string):
    words = string.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest= word
    return longest
n=SoLong("ferrari sf-23 is the fastest car in the the grid,so i think scuderia_ferrari willbe world champ in this year")
print("the longest word is ",n)