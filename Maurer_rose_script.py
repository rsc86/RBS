import bpy
import bmesh
import math
from mathutils import Vector

def to_radians(degrees):
    return round(degrees * (math.pi/180), 7)

def to_degrees(radians):
    return radians * (180/math.pi)


# Petals
petals = 2
# Degrees
degrees = 29


def create_rose_pattern(n, d, radius=1):
    list_of_vectors = []
    r_scalar = radius * 1.3
    for theta in range(361):
        k = theta * d * math.pi / 180
        r = r_scalar * math.sin(n * k)
        x = r * math.cos(k)
        y = r * math.sin(k)
        z = 0
        list_of_vectors.append(Vector((x,y,z)))
    return list_of_vectors 
 
def create_constructor_lines(n, d, radius=1):  
    list_of_vectors = [] 
    r_scalar = radius * 1.3
    for theta in range(361):
        k = theta * math.pi / 180
        r = r_scalar * math.sin(n * k)
        x = r * math.cos(k)
        y = r * math.sin(k)
        z = 0
        list_of_vectors.append(Vector((x,y,z)))    
    return list_of_vectors


def make_poly_line(objname, curvename, cList):
    w = 1
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')
    curvedata.dimensions = '3D'

    objectdata = bpy.data.objects.new(objname, curvedata)
    objectdata.location = (0,0,0) #object origin
    bpy.context.collection.objects.link(objectdata)

    polyline = curvedata.splines.new('POLY')
    polyline.points.add(len(cList)-1)
    for num in range(len(cList)):
        x, y, z = cList[num]
        polyline.points[num].co = (x, y, z, w)
    
    

make_poly_line("Pattern", "MaurerRosePattern", create_rose_pattern(petals, degrees))

make_poly_line("Constructor", "MaurerRoseConstructorLines", create_constructor_lines(petals, degrees))