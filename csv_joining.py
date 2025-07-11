import pandas as pd 
import csv

def tsv_to_csv(tsv_file_path, csv_file_path):
    with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsvfile, \
         open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        writer = csv.writer(csvfile, delimiter=',')
        for row in reader:
            writer.writerow(row)


tsv_to_csv("D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\peptide.tsv","D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\peptide.csv")

df = pd.read_csv("D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\peptide.csv")
dff = df.drop(columns=['Charges','Probability','Spectral Count','Intensity','Entry Name','Gene','Protein Description','Mapped Genes','Mapped Proteins','Qvalue','Is Decoy','Is Contaminant'])
dff.to_csv("D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\peptide_RDY.csv")


tsv_to_csv("D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\protein.tsv","D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\protein.csv")

df = pd.read_csv("D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\protein.csv")
columns_to_keep = ['Protein ID','Coverage','Total Peptides']  
df = df[[col for col in df.columns if col in columns_to_keep]]
df.to_csv("D:\\MG\\CODES\\ALL_3_NO-CRYSTAL\\protein_RDY.csv", index=False)












