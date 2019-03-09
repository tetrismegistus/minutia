from common.grids import distance, grid
from common.Animation import Animation
from common import runtimedefs
from demos import display_maze
from algorithms.mazes import binary_tree, aldous_broder, wilsons, hybrids, sidewinder
import seaborn


# m = distance.XRayDistanceGrid(100, 100, palette="hls", walls=False, cell_size=3)
# m = distance.XRayDistanceGrid(100, 100, palette="cubehelix")
animation = Animation()
m = distance.XRayDistanceGrid(10, 10)
m = wilsons.wilsons(m, animation=animation)
m.animation = animation
m.fill_distances(m.random_cell())
#m.to_img().save('test.png')
m.animation.save_gif()
animation.save_gif()

# Todo: dynamic resolution based generation
# Todo: optimize gif size
# Todo: make functions for my most common operations in demos
# Todo: Create UI for generating and previewing and saving mazes, including serializing grid object
# Todo: go through and make sure all algorithms receive animation object

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
