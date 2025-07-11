import matplotlib.pyplot as plt
import pandas as pd


df1 = pd.read_csv("protein_4_RDY.csv")
df2 = pd.read_csv("9\\protein_basic_full.csv")


merged = pd.merge(df1, df2, on='Protein ID', suffixes=('_file1', '_file2'))
merged_sorted = merged.sort_values(by="Coverage_file1", ascending=False)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

ax1.scatter(merged_sorted["Protein ID"], merged_sorted["Coverage_file1"], color='blue', label='Coverage (protein_4_RDY.csv)')
ax1.scatter(merged_sorted["Protein ID"], merged_sorted["Coverage_file2"], color='orange', label='Coverage (protein_basic_full.csv)')
ax1.set_title("Coverage Comparison per Protein")
ax1.set_ylabel("Coverage")
ax1.legend()
ax1.tick_params(axis='x', rotation=90)


ax2.scatter(merged_sorted["Protein ID"], merged_sorted["Total Peptides_file1"], color='green', label='Total Peptides (protein_4_RDY.csv)')
ax2.scatter(merged_sorted["Protein ID"], merged_sorted["Total Peptides_file2"], color='red', label='Total Peptides (protein_basic_full.csv)')
ax2.set_title("Total Peptides Comparison per Protein")
ax2.set_ylabel("Total Peptides")
ax2.set_xlabel("Protein ID")
ax2.legend()
ax2.tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()










