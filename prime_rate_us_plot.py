import plotly.express as px
import pandas as pd


data = pd.read_csv('data/us_prime_rates.csv')

years = data['year'].tolist()
rates = data['rate'].tolist()

# Create an interactive line plot
fig = px.line(x=years, y=rates, labels={"x": "Year", "y": "Prime Rate (%)"}, title="U.S. Prime Rate (1975–2024)")
fig.update_traces(mode="lines+markers")

# Show the plot in a web browser
fig.show()
#Export
#fig.write_html("prime_rate_chart.html")