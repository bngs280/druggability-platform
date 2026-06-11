import os
import requests

AF_URL = "https://alphafold.ebi.ac.uk/files/AF-{}-F1-model_v6.pdb"
        # https://alphafold.ebi.ac.uk/files/AF-{uniprot}-F1-model_v6.pdb
def download_pdb(uniprot_id, out_dir="data/pdb"):
    os.makedirs(out_dir, exist_ok=True)

    url = AF_URL.format(uniprot_id)

    out_path = os.path.join(out_dir, f"{uniprot_id}.pdb")

    r = requests.get(url)

    if r.status_code != 200:
        raise Exception(f"Structure not found for {uniprot_id}")

    with open(out_path, "w") as f:
        f.write(r.text)

    return out_path
