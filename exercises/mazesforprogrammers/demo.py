from common.grids import distance
from common import runtimedefs
from algorithms.mazes import binary_tree


m = distance.AnimatedDistanceGrid(100, 100)
runtimedefs.DEFAULTALGO(m)
m.fill_distances(m[m.rows - 1, 0])
m.save_gif()

# Todo: dynamic resolution based generation
# Todo: optimize gif size
# Todo: change get_color to RGB walk
# Todo: change default gradient to not have background color
# Todo: dwell on final image a bit longer before looping

"""
animated gif notes:
larger mazes make huge files with a slowish animation 
post production mitigation currently done as

gifsicle --colors=255 animated.gif -o output.gif                        | prepare for frame removal
gifsicle -U output.gif `seq -f "#%g" 0 2 1000` -O2 -o output2.gif       | remove frames, can run multiple times
                                                                        | in this example 1000 is num of frames                                                                         
gifsicle -O3 < fast.gif fast2.gif                                       | further compression


DO NOT DELETE -- this will be important later
target_h = 2160
target_w = 1080
img_w = cell_size * self.columns
img_h = cell_size * self.rows


Consider I have a target width

I want the largest cell size possible where cell_size *

x * c = 2160
x * r = 1080

c = 2r

so I want about 100 rows
2*100

2160 = 10.8 * 200
1080 = 10.8 * 100

108
"""
