import os
import glob
import subprocess

PDB_DIR = "data/pdb"


def run_fpocket(pdb_file):

    protein = os.path.splitext(
        os.path.basename(pdb_file)
    )[0]

    output_dir = os.path.join(
        PDB_DIR,
        f"{protein}_out"
    )

    # Skip if already processed
    if os.path.exists(output_dir):
        print(f"[SKIP] {protein}")
        return

    cmd = [
        "fpocket",
        "-f",
        pdb_file
    ]

    try:
        subprocess.run(
            cmd,
            check=True
        )

        print(f"[DONE] {protein}")

    except subprocess.CalledProcessError:

        print(f"[FAILED] {protein}")


def main():

    pdb_files = sorted(
        glob.glob(
            os.path.join(
                PDB_DIR,
                "*.pdb"
            )
        )
    )

    print(f"Total PDB files: {len(pdb_files)}")

    for i, pdb in enumerate(pdb_files, start=1):

        protein = os.path.basename(pdb)

        print(f"\n[{i}/{len(pdb_files)}] {protein}")

        run_fpocket(pdb)


if __name__ == "__main__":
    main()