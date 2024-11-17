import pygal
import pandas as pd


data = pd.read_csv('data/us_prime_rates.csv')

years = data['year'].tolist()
rates = data['rate'].tolist()

# Create a line chart
line_chart = pygal.Line(title="U.S. Prime Rate (1975–2024)", x_title="Year", y_title="Prime Rate (%)")

# Add data to the chart
line_chart.x_labels = map(str, years)  # X-axis labels as years
line_chart.add("Prime Rate", rates)    # Add the rates as a series

# Save to file and render in a browser
line_chart.render_to_file("prime_rate_chart.svg")
print("Chart saved as prime_rate_chart.svg")
