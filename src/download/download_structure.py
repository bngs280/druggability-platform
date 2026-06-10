import os
import requests
import pandas as pd

CSV_FILE = "data/processed/proteins_final.csv"
SAVE_DIR = "data/pdb"

os.makedirs(SAVE_DIR, exist_ok=True)


def download_structure(uniprot):

    outfile = os.path.join(
        SAVE_DIR,
        f"{uniprot}.pdb"
    )

    # Skip if already downloaded
    if os.path.exists(outfile):
        print(f"[SKIP] {uniprot}")
        return

    url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot}-F1-model_v6.pdb"

    try:
        r = requests.get(url, timeout=30)

        if r.status_code != 200:
            print(f"[FAILED] {uniprot}")
            return

        with open(outfile, "wb") as f:
            f.write(r.content)

        print(f"[DOWNLOADED] {uniprot}")

    except Exception as e:
        print(f"[ERROR] {uniprot} : {e}")


def main():

    df = pd.read_csv(CSV_FILE)

    # Change this if your column name is different
    uniprot_ids = df["UniProt"].dropna().unique()

    print(f"Total proteins: {len(uniprot_ids)}")

    for i, uniprot in enumerate(uniprot_ids, start=1):

        print(f"\n[{i}/{len(uniprot_ids)}] {uniprot}")

        download_structure(uniprot)


if __name__ == "__main__":
    main()