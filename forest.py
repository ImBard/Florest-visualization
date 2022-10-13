import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import cm
import numpy as np
from main import forests


fig = plt.figure()

ax = plt.axes()
fig.set_size_inches(7, 3.5)

img = plt.imshow(forests[0], cmap="Reds", interpolation="nearest")


forests[0][forests[0] == 254] = 0.0

ourcmap = cm.get_cmap("Greens", 101)
newcolors = ourcmap(np.linspace(0,1,101))
background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
newcolors[:1, :] = background_colour
newcmp_forests = ListedColormap(newcolors)


ax.axis('off')
plt.show()

fig = plt.figure(facecolor='#FCF6F5FF')
ax = plt.axes()
fig.set_size_inches(7, 3.5)
ax.patch.set_facecolor('#FCF6F5FF')

imgs = plt.imshow(forests[0],
                  cmap=newcmp_forests,
                  interpolation='nearest')

ax.set_xlim(2000, 43500)
ax.set_ylim(19500, 800)
ax.axis('off')
plt.show()