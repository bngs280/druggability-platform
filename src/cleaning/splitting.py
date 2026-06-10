import csv

input_file = "data/raw/protein_comp.csv"
output_file = "data/raw/proteins_clean.csv"

rows = []

with open(input_file, "r", encoding="utf-8") as f:

    # skip header
    next(f)

    for line in f:

        line = line.strip()

        if not line:
            continue

        # split using LAST comma only
        target, accessions = line.rsplit(",", 1)

        rows.append([target, accessions])

with open(output_file, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(["Target", "Accessions"])

    writer.writerows(rows)

print("Done")
print("Rows:", len(rows))

