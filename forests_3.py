from matplotlib.colors import ListedColormap
from matplotlib import cm
import numpy as np
from main import forests

forests[0][forests[0] == 254] = 0.0

ourcmap = cm.get_cmap("Greens", 101)
newcolors = ourcmap(np.linspace(0,1,101))
background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
newcolors[:1, :] = background_colour
newcmp_forests = ListedColormap(newcolors)