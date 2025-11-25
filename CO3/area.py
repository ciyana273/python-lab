from Graphics.RectFunctions import RectArea
from Graphics.RectFunctions import RectPerimeter
from Graphics.CirFunctions import CirPerimeter
from Graphics.CirFunctions import CirArea
from Graphics.DGraphics.SphereFunctions import SpArea
from Graphics.DGraphics.SphereFunctions import SpPerimeter 
from Graphics.DGraphics.CuboidFunctions import CubArea
from Graphics.DGraphics.CuboidFunctions import CubPerimeter
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
print("Rectangle Area =", RectArea(l,b))
print("Rectangle Perimeter =", RectPerimeter(l,b))
r=int(input("Enter radius of Circle:"))
print("CircleArea=",CirArea(r))
print("Circle Perimeter=",CirPerimeter(r))
r=int(input("Enter radius of Sphere:"))
print("Sphere Area=",SpArea(r))
print("Sphere Volume=",SpPerimeter(r))
l=int(input("Enter cuboid length:"))
b=int(input("Enter cuboid breadth:"))
h=int(input("Enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid Perimeter=",CubPerimeter(l,b,h))

