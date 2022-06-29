import pandas as pd
import matplotlib.pyplot as plt

file = "results/MREC_MAE_60/expected_values.csv"
df = pd.read_csv(file)

measured = df['Measured']
expected = df['Expected']

plt.figure(figsize=(10,10))
plt.scatter(measured, expected, c='crimson')

p1 = max(max(measured), max(expected))
p2 = min(min(measured), min(expected))
plt.plot([p1, p2], [p1, p2], 'b-')
plt.xlabel('Measured Gaze Duration', fontsize=15)
plt.ylabel('Expected Gaze Duration', fontsize=15)
plt.axis('equal')

plt.savefig("results/Measured_vs_expected.png")

