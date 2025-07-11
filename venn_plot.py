from venn import venn
import matplotlib.pyplot as plt
import pandas as pd



df1 = pd.read_csv("D:\\MG\\CODES\\9_FULL_CRYSTAL-C\\peptide_basic_full_RDY.csv")
df2 = pd.read_csv("D:\\MG\\CODES\\10_FULL_NO-C\\peptide_full_no-c_RDY.csv")
df3 = pd.read_csv("D:\\MG\\CODES\\P46_2_FULL_CRYSTAL\\peptide_2_full_c_RDY.csv")  
df4 = pd.read_csv("D:\\MG\\CODES\\P46_2_FULL_NO-CRYSTAL\\peptide_2_full_no-c_RDY.csv")
df5 = pd.read_csv("D:\\MG\\CODES\\P46_3_FULL_CRYSTAL\\peptide_3_full_c_RDY.csv")  
df6 = pd.read_csv("D:\\MG\\CODES\\P46_3_FULL_NO-CRYSTAL\\peptide_3_full_no-c_RDY.csv")

data = {

    "P46_2_FULL_CRYSTAL-C": set(df4["Peptide"]),  
    "P46_2_FULL_NO-C": set(df4["Peptide"]),

}


data = {k: v for k, v in data.items() if v is not None}

venn(data)
plt.title("Venn Diagram of Peptides")
plt.show()
