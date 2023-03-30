import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0,2*np.pi,100)
s = np.sin(x)
c = np.cos(x)

# Create plot
plt.plot(x, s, 'r', linewidth=2)
plt.plot(x, c, 'b', linewidth=2)

# Set limits
plt.xlim(-1,7)
plt.ylim(-2,2)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos')

