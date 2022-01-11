class Area():
    @staticmethod
    def rectangle(side1, side2):
        surface_area = side1*side2
        return surface_area
    
    @staticmethod
    def triangle(base, height):
        surface_area2 = (base*height)/2
        return surface_area2
    
    @staticmethod
    def circle(radius):
        surface_area3 = (radius)**2*3.14
        return surface_area3
    
    
print(Area.rectangle(4,7))
print(Area.triangle(6,2))
print(Area.circle(3))