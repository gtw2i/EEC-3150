import matplotlib.pyplot as plt
import numpy as np

# Define the function to plot
def f(x, y):
    return np.exp(-x**2 - y**2)

# Define the x and y ranges
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)

# Create a meshgrid from the x and y ranges
X, Y = np.meshgrid(x, y)

# Evaluate the function over the meshgrid
Z = f(X, Y)

# Create the figure and axes objects
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z)

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of exp(-x^2-y^2)')
