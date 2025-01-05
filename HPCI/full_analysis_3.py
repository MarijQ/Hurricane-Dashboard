import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('storms.csv')

# Keep records from 2004 onwards and where diameter values are recorded
df = df[df['year'] >= 2004].dropna(subset=['tropicalstorm_force_diameter', 'hurricane_force_diameter'])

# Define the relative KE calculation function
def calculate_relative_ke(row):
    diameter = row['tropicalstorm_force_diameter']
    return diameter ** 2 * row['wind'] ** 3

# Calculate relative KE for each row
df['relative_ke'] = df.apply(calculate_relative_ke, axis=1)

# Define a unique identifier for each storm
df['storm_id'] = df['name'] + "_" + df['year'].astype(str)

# Group by 'status' and 'storm_id', then calculate average KE for each storm
ke_grouped = df.groupby(['status', 'storm_id'])['relative_ke'].mean().reset_index()

# Calculate average relative KE for each status
ke_status_avg = ke_grouped.groupby('status')['relative_ke'].mean()

# Plot the results in a bar chart
ke_status_avg.plot(kind='bar', figsize=(12, 7))
plt.title('Average Relative Kinetic Energy by Storm Status')
plt.xlabel('Storm Status')
plt.ylabel('Average Relative Kinetic Energy')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
