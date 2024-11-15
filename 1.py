class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def __add__(self, other):
        return Box(self.length + other.length, 
                   self.width + other.width, 
                   self.height + other.height)

    def __repr__(self):
        return f"Box({self.length}, {self.width}, {self.height}, V={self.volume()})"

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __eq__(self, other):
        return self.volume() == other.volume()

box1 = Box(2, 3, 4)
box2 = Box(1, 1, 1)

print(box1)  
print(box2)  

box3 = box1 + box2
print(box3)

print(box1 > box2)  
print(box1 == box2) 
