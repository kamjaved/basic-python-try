import math
import random
from string import ascii_lowercase # u can import sepciic method like this and use like variable in code

print(math.sqrt(4))
print(random.randint(1,20))
print(ascii_lowercase) # using module method as like normal variable 


# graph.py
import matplotlib.pyplot as plt

# Create data for the graph
x_values = list(range(0, 11))
y_values = [val**2 for val in x_values]

# Add labels to the axes
plt.xlabel("X Axis")
plt.ylabel("Y Axis (X^2)")

# Plot the data
plt.plot(x_values, y_values)

# Display the graph
plt.show()