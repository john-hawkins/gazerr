import pandas as pd
import matplotlib.pyplot as plt

file = "results/MREC_MAE_70/expected_values.csv"
file2 = "results/MREC_MAE_Biased_70/expected_values.csv"

df = pd.read_csv(file)
df2 = pd.read_csv(file2)

measured = df['Measured']
expected = df['Expected']
measured2 = df2['Measured']
expected2 = df2['Expected']

fig = plt.figure(figsize=(12,6))

ax = fig.add_subplot()
ax.set_title('Measured Duration Vs Expected Duration')
ax.plot(measured, expected, c='orchid', label="Uniform Fixation Error")
ax.plot(measured2, expected2, c='teal', label="Biased Fixation Error", linestyle='dashed')
p1 = max(max(measured), max(expected))
p2 = min(min(measured), min(expected))
ax.plot([p1, p2], [p1, p2], c='lightsteelblue', linestyle='dotted', label='Ideal' )
ax.set_xlabel('Measured Gaze Duration', fontsize=15)
ax.set_ylabel('Expected Gaze Duration', fontsize=15)
ax.legend( prop={'size': 15} )

plt.savefig("results/Measured_vs_expected.png")


