import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for ages
np.random.seed(0)
ages = np.random.randint(0, 100, 1000)  # Generating 1000 random ages between 0 and 100

# Define bins for the histogram
bins = np.arange(0, 101, 10)  # Define bins for age groups (0-9, 10-19, 20-29, ..., 90-99, 100)

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=bins, edgecolor='black', alpha=0.7)

# Customize the plot
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
