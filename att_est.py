"""
This example loads the tetra3 default database and solves for every image in the tetra3/test_data directory.

Note: Requires PIL (pip install Pillow)
"""
# import sys
# sys.path.append('..')
from tetra3 import Tetra3, get_centroids_from_image
from PIL import Image
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Create instance and load default_database (built with max_fov=12 and the rest as default)
t3 = Tetra3('default_database')

# Path where images are
path = Path('screenshots/')
for impath in path.glob('*.png'):
    print('Solving for image at: ' + str(impath))
    with Image.open(str(impath)) as img:
        # https://www.geeksforgeeks.org/python-channel-drop-using-pillow/
        # A 12-value tuple which is a transform matrix for dropping 
        # green channel (in this case)
        print(img)
        matrix = ( 1, 0, 0, 0,
                0, 1, 0, 0,
                0, 0, 1, 0)
        imgRGB = img.convert("RGB")#, matrix)
        print(imgRGB)
        centroids = get_centroids_from_image(image = np.asarray(imgRGB))
        print('centroids: ' + str(centroids))

        im = plt.imread(impath)
        implot = plt.imshow(im)

        centroids_x = centroids[:,0]
        centroids_y = centroids[:,1]
        plt.scatter(centroids_y, centroids_x, s=80, facecolors='none', edgecolors='r')

        plt.show()

        solved = t3.solve_from_image(imgRGB, fov_estimate=14, fov_max_error=10, match_radius=0.5, match_threshold=1e-4)  # Adding e.g. fov_estimate=11.4, fov_max_error=.1 improves performance
    print('Solution: ' + str(solved))