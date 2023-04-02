class veichle():
    name = ''
    color = ''
    year = 0
    milage = 0
    capacity = 0
    def set_capacity(self , capacity):
        self.capacity = capacity

class truck(veichle):
    def __init__(self, name,color,year,milage) :
        self.name = name
        self.color = color
        self.year = year
        self.milage = milage
       


maul = truck("maul","pink",2003,9)
maul.set_capacity(80)
print(maul.name,maul.color,maul.year,maul.milage,maul.capacity)

