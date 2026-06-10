import subprocess
import os

def run_colabfold(fasta_file):

    output_dir = "data/pdb"

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    cmd = [
        "colabfold_batch",
        fasta_file,
        output_dir
    ]

    subprocess.run(
        cmd,
        check=True
    )

if __name__ == "__main__":

    run_colabfold(
        "data/raw/test.fasta"
    )