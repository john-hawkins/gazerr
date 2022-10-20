import pandas as pd
import matplotlib.pyplot as plt

file = "results/MREC_MErr_70/expected_values.csv"
file2 = "results/MREC_MErr_Biased_70/expected_values.csv"
file3 = "results/MREC_MErr_Biased_Precise_70/expected_values.csv"

df = pd.read_csv(file)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

measured = df['Measured']
expected = df['Expected']
measured2 = df2['Measured']
expected2 = df2['Expected']
measured3 = df3['Measured']
expected3 = df3['Expected']

fig = plt.figure(figsize=(12,6))

ax = fig.add_subplot()
ax.set_title('Measured Duration Vs Expected Duration - 70 Pixel Mean Error')
ax.plot(measured, expected, c='firebrick', label="Uniform Fixation Error")
ax.plot(measured2, expected2, c='seagreen', label="Biased Fixation Error", linestyle='dashed')
ax.plot(measured3, expected3, c='darkorchid', label="Precise Biased Fixation Error", linestyle='dotted')
p1 = max(max(measured), max(expected))
p2 = min(min(measured), min(expected))
ax.plot([p1, p2], [p1, p2], c='lightsteelblue', linestyle='dotted', label='Ideal' )
ax.set_xlabel('Measured Gaze Duration', fontsize=15)
ax.set_ylabel('Expected Gaze Duration', fontsize=15)
ax.legend( prop={'size': 15} )

plt.savefig("results/Measured_vs_expected.png")

