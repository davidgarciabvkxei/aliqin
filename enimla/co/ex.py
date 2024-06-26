import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Create a random dataset
df = np.random.randn(30, 30)

# Plot a diverging heatmap centered at 1
sns.heatmap(df, center=1)
plt.show()
