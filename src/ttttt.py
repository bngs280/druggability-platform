import pandas as pd

# Load files
df1 = pd.read_csv("/home/deepak/druggability-platform/data/features/features.csv")
df2 = pd.read_csv("/home/deepak/druggability-platform/data/features/file2.csv")

# If Compounds has multiple values separated by |
df2["Compounds"] = df2["Compounds"].astype(str).str.split("|")

# explode into multiple rows
df2 = df2.explode("Compounds")

# optional cleanup
df2["Compounds"] = df2["Compounds"].str.strip()

# merge on UniProt
merged = df1.merge(
    df2[["UniProt", "Compounds"]],
    on="UniProt",
    how="left"
)

# rename column if needed
merged = merged.rename(columns={"Compounds": "Compound"})

# save result
merged.to_csv("file1_with_compounds.csv", index=False)

print(merged)