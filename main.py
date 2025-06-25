import matplotlib.pyplot as plt
import numpy as np

# Criteria for trade-off analysis
criteria = ['Effectiveness', 'Survivability', 'Interoperability', 'Sustainment', 'Complexity']
n_criteria = len(criteria)

# Example scores for three options (scale: 0–10)
option_1 = [8, 6, 7, 5, 4]
option_2 = [6, 8, 6, 7, 5]
option_3 = [7, 5, 8, 6, 6]

# Complete the loop for radar chart
option_1 += option_1[:1]
option_2 += option_2[:1]
option_3 += option_3[:1]

# Angle for each axis
angles = np.linspace(0, 2 * np.pi, n_criteria, endpoint=False).tolist()
angles += angles[:1]

# Set up the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot each option
ax.plot(angles, option_1, label='Option 1: UAS Integration', linewidth=2)
ax.fill(angles, option_1, alpha=0.1)

ax.plot(angles, option_2, label='Option 2: Improved SATCOM', linewidth=2)
ax.fill(angles, option_2, alpha=0.1)

ax.plot(angles, option_3, label='Option 3: ISR Fusion Middleware', linewidth=2)
ax.fill(angles, option_3, alpha=0.1)

# Add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria)
ax.set_yticklabels([])  # Hide radial labels for clarity
ax.set_title("Trade Study Comparison – Example Radar Chart", size=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 0.25))

plt.tight_layout()
plt.show()
