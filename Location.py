import math

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def distance_from_origin(self):
        distance = math.sqrt(self.latitude ** 2 + self.longitude ** 2)
        return distance

    def distance_between_objects(self, obj2):
        distance = math.sqrt((obj2.latitude - self.latitude)**2 + (obj2.longitude - self.longitude)**2)
        return distance

location1 = Location(3, 0)  
location2 = Location(4, 0)  
jarakawal=location1.distance_from_origin()
distance = location1.distance_between_objects(location2)

print("jarak awal",jarakawal)
print("jarak antar objek", distance)
print("L200210135 Naufal Hanief Mafaza")