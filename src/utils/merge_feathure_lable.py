import pandas as pd
import numpy as np

# Read files
file1 = pd.read_csv("/home/deepak/druggability-platform/data/features/features.csv")
file2 = pd.read_csv("/home/deepak/druggability-platform/data/processed/proteins_final.csv")

# Keep only required columns
file2 = file2[["UniProt", "Compounds"]]

# Merge on UniProt
df = file1.merge(file2, on="UniProt", how="left")

# Convert Compounds to numeric
df["Compounds"] = pd.to_numeric(df["Compounds"], errors="coerce")

# Create label
df["label"] = np.where(
    df["Compounds"].fillna(0) >= 1,
    1,
    0
)

# Remove Compounds column if you only want label
df = df.drop(columns=["Compounds"])

# Save
df.to_csv("data/features/features_with_label.csv", index=False)

print(df.head())
print("Total rows:", len(df))
print(df["label"].value_counts())