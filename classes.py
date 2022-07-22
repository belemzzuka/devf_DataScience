class MyClassExample:
    lat = 400
    long = 300
    def __init__(self, place):
        self.place = place
    
    def getPlace(self):
        print(self.place)

obj = MyClassExample("Queretaro")

print(obj.lat)
print(obj.long)
print(obj.place)
print(obj.place)