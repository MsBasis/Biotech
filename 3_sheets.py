import pandas as pd

#1 - all of them
#2 - halfs
#3 - full

half_C = pd.read_csv("D:\\MG\\CODES\\4_HALF_CRYSTAL-C\\protein_4_RDY.csv")
half = pd.read_csv("D:\\MG\\CODES\\4_HALF_NO-C\\protein_half_no-c_RDY.csv")
full_C = pd.read_csv("D:\\MG\\CODES\\9_FULL_CRYSTAL-C\\protein_basic_full_RDY.csv")  
full = pd.read_csv("D:\\MG\\CODES\\10_FULL_NO-C\\protein_full_no-c_RDY.csv")  


set1 = set(half_C["Protein ID"])
set2 = set(half["Protein ID"])
set3 = set(full_C["Protein ID"])
set4 = set(full["Protein ID"])


all_of_them = set1 & set2 & set3 & set4
halfs = set1 & set2 - (set3|set4)
fulls = set3 & set4 - (set1|set2)

df_all = half_C[half_C["Protein ID"].isin(all_of_them)]
df_halfs = half_C[half_C["Protein ID"].isin(halfs)]
df_fulls = full_C[full_C["Protein ID"].isin(fulls)]

with pd.ExcelWriter("D:\\MG\\CODES\\venn_filtered_proteins.xlsx", engine="xlsxwriter") as writer:
    df_all.to_excel(writer, sheet_name="Shared_All_4", index=False)
    df_halfs.to_excel(writer, sheet_name="Only_Halfs", index=False)
    df_fulls.to_excel(writer, sheet_name="Only_Fulls", index=False)

