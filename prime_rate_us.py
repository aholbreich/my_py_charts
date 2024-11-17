import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/us_prime_rates.csv')

years = data['year'].tolist()
rates = data['rate'].tolist()

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(years, rates, marker='o', linestyle='-', linewidth=2)

# Add labels, title, and grid
plt.title("U.S. Prime Rate (1975–2024)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Prime Rate (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
