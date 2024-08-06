import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Generate sample data
np.random.seed(0)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(1, 1.5, 1000)

# Perform KDE
data = np.vstack([x, y])
kde = gaussian_kde(data)

# Create a grid over which to evaluate the KDE
xmin, xmax = x.min() - 1, x.max() + 1
ymin, ymax = y.min() - 1, y.max() + 1
X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
Z = np.reshape(kde(positions).T, X.shape)

# Plot the results
fig, ax = plt.subplots()
ax.imshow(np.rot90(Z), cmap=plt.cm.viridis, extent=[xmin, xmax, ymin, ymax])
ax.plot(x, y, 'k.', markersize=2)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.show()
