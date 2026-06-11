######### split ############

import pandas as pd

INPUT = "data/raw/proteins_clean.csv"
OUTPUT = "data/processed/proteins_final.csv"

df = pd.read_csv(INPUT)

rows = []

for _, row in df.iterrows():

    target = str(row["Target"]).strip()
    accessions = str(row["Accessions"]).strip()
    compounds = row["Compounds"]

    proteins = accessions.split("|")

    for protein in proteins:

        protein = protein.strip()

        if protein:

            rows.append({
                "Target": target,
                "UniProt": protein,
                "Compounds": compounds
            })

final_df = pd.DataFrame(rows)

# Remove duplicate UniProt IDs
# If the same UniProt appears multiple times, keep the first occurrence
final_df = final_df.drop_duplicates(subset=["UniProt"], keep="first")

# Sort alphabetically
final_df = final_df.sort_values("UniProt")

# Reset index
final_df = final_df.reset_index(drop=True)

# Save
final_df.to_csv(
    OUTPUT,
    index=False
)

print("Total proteins:", len(final_df))
print(final_df.head())

# ######### split ############
# import pandas as pd

# INPUT = "data/raw/proteins_clean.csv"
# OUTPUT = "data/processed/proteins_final.csv"

# df = pd.read_csv(INPUT)

# rows = []

# for _, row in df.iterrows():

#     target = str(row["Target"]).strip()
#     accessions = str(row["Accessions"]).strip()

#     proteins = accessions.split("|")

#     for protein in proteins:

#         protein = protein.strip()

#         if protein:

#             rows.append({
#                 "Target": target,
#                 "UniProt": protein
#             })

# final_df = pd.DataFrame(rows)

# # Remove duplicate UniProt IDs
# final_df = final_df.drop_duplicates(subset=["UniProt"])

# # Sort alphabetically
# final_df = final_df.sort_values("UniProt")

# final_df.to_csv(
#     OUTPUT,
#     index=False
# )

# print("Total proteins:", len(final_df))
# print(final_df.head())