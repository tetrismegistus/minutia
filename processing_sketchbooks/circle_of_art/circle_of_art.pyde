from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def setup():
    size(600, 600)

        
def draw():
    
    translate(width/2, height/2)
    
    inner_circle_r = 200
    mid_circle_r = inner_circle_r + 50
    outer_circle_r = mid_circle_r + 100    
    main_triangle = tri(100)    
    
    circle(0, 0, inner_circle_r)
    circle(0, 0, mid_circle_r)
    circle(0, 0, outer_circle_r)
    
    intersection_circle_r = (inner_circle_r - 75)/2
    corners = get_triangle_corners(main_triangle, intersection_circle_r)
    translate(corners[1].x, corners[1].y)
    draw_five_pointed_star(10)
            
    
                    
def get_triangle_corners(main_triangle, r):
    side1 = get_corner_points(main_triangle[0], main_triangle[1], r)
    side2 = get_corner_points(main_triangle[1], main_triangle[2], r)
    side3 = get_corner_points(main_triangle[2], main_triangle[0], r)
    newside1 = (side1[1], side2[0])
    newside2 = (side2[1], side3[0])
    newside3 = (side3[1], side1[0])
    # each of these is a triangle, I wish to find the center of
    
    corners = [(Point(newside1[0].x, newside1[0].y),             
                Point(newside3[0].x, newside3[0].y),
                Point(main_triangle[0].x, main_triangle[0].y)),
               (Point(newside3[1].x, newside3[1].y),             
                Point(newside2[0].x, newside2[0].y),
                Point(main_triangle[1].x, main_triangle[1].y)),
               (Point(newside2[1].x, newside2[1].y),
                Point(newside1[1].x, newside1[1].y),
                Point(main_triangle[2].x, main_triangle[2].y))]
    centroids = []
    for c in corners:
        centroids.append(get_centroid(c))
    return centroids

def get_centroid(tri):                
    ox = (tri[0].x + tri[1].x + tri[2].x) / 3
    oy = (tri[0].y + tri[1].y + tri[2].y) / 3
    return Point(ox, oy)

                                                            
    
def draw_five_pointed_star(tri_size):
    pentagon = polygon_vertices(5, tri_size)
    for idx, vertice in enumerate(pentagon):
        next_v = pentagon[(idx + 2) % len(pentagon)]
        line(vertice[0], vertice[1], next_v[0], next_v[1])


def get_corner_points(v1, v2, r=125/2):
    def sgn(x): return -1 if x < 0 else 1         
    dx = v2.x - v1.x
    dy = v2.y - v1.y
    dr = sqrt(dx**2 + dy**2)
    D = (v1.x * v2.y) - (v2.x * v1.y)
    x1 = (D * dy + sgn(dy) * dx * sqrt(r**2 * dr**2 - D**2)) / dr**2
    x2 = (D * dy - sgn(dy) * dx * sqrt(r**2 * dr**2 - D**2)) / dr**2
    y1 = (-D * dx + abs(dy) * sqrt(r**2 * dr**2 - D**2)) / dr**2
    y2 = (-D * dx - abs(dy) * sqrt(r**2 * dr**2 - D**2)) / dr**2
    return (Point(x1, y1), Point(x2, y2))


def tri(length):
    noFill()
    v1 = Point(0, -length)
    v2 = Point(-length * sqrt(3)/2, length / 2)
    v3 = Point(length * sqrt(3)/2, length/2)
    triangle(v1.x, v1.y,
             v2.x, v2.y, 
             v3.x, v3.y)
    return [v1, v2, v3]        
                
def polygon_vertices(sides, sz):
    noFill()    
    vertices = []
    for i in range(sides):
        step = radians(360/sides)
        x, y = sz*cos(i*step), sz*sin(i*step)    
        vertices.append((x, y))    
    return vertices
    
