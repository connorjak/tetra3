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


t3 = Tetra3()

t3.generate_database(40,"hip_40fov",'hip_main')