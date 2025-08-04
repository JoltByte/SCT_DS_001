import matplotlib.pyplot as plt
import numpy as np

# Sample age data
ages = [22, 25, 30, 22, 25, 30, 35, 40, 45, 35, 38, 28, 31, 33, 30, 29, 26, 25, 35, 42]

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(ages, bins=6, color='skyblue', edgecolor='black')
plt.title('Age Distribution in the Population')
plt.xlabel('Age')
plt.ylabel('Number of People')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
