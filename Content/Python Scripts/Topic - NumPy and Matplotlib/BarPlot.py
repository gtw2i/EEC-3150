import matplotlib.pyplot as plt

# Sample data
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

# Create bar plot
#plt.bar(x, y, width=0.7)
plt.barh(x, y)

# Add labels and title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Title of the bar plot')

# Display the plot
plt.show()