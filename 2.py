class Color:
    def __init__(self, red, green, blue):
        if not all(0 <= value <= 255 for value in (red, green, blue)):
            raise ValueError("Значения RGB должны быть в диапазоне от 0 до 255.")
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, other):
        if isinstance(other, Color):
            return Color((self.red + other.red) % 256,
                         (self.green + other.green) % 256,
                         (self.blue + other.blue) % 256)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Color):
            return Color((self.red - other.red) % 256,
                         (self.green - other.green) % 256,
                         (self.blue - other.blue) % 256)
        return NotImplemented

    def __repr__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"

    def __str__(self):
        return self.__repr__()

color1 = Color(100, 150, 200)
color2 = Color(200, 100, 50)

print(color1)  
print(color2)  

color3 = color1 + color2
print(color3)  

color4 = color1 - color2
print(color4) 

colors = [color1, color2, color3, color4]
print(colors) 