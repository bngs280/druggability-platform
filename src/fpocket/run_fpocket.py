import os
import glob
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed

PDB_DIR = "data/pdb"

# Change according to your machine
N_WORKERS = 8


def run_fpocket(pdb_file):

    protein = os.path.splitext(
        os.path.basename(pdb_file)
    )[0]

    output_dir = os.path.join(
        PDB_DIR,
        f"{protein}_out"
    )

    # Skip already processed
    if os.path.exists(output_dir):
        return f"[SKIP] {protein}"

    cmd = [
        "fpocket",
        "-f",
        pdb_file
    ]

    try:
        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        return f"[DONE] {protein}"

    except subprocess.CalledProcessError:
        return f"[FAILED] {protein}"


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
    print(f"Using {N_WORKERS} parallel workers\n")

    with ProcessPoolExecutor(max_workers=N_WORKERS) as executor:

        futures = {
            executor.submit(run_fpocket, pdb): pdb
            for pdb in pdb_files
        }

        completed = 0

        for future in as_completed(futures):

            completed += 1

            print(
                f"[{completed}/{len(pdb_files)}] "
                f"{future.result()}"
            )


if __name__ == "__main__":
    main()


# import os
# import glob
# import subprocess

# PDB_DIR = "data/pdb"


# def run_fpocket(pdb_file):

#     protein = os.path.splitext(
#         os.path.basename(pdb_file)
#     )[0]

#     output_dir = os.path.join(
#         PDB_DIR,
#         f"{protein}_out"
#     )

#     # Skip if already processed
#     if os.path.exists(output_dir):
#         print(f"[SKIP] {protein}")
#         return

#     cmd = [
#         "fpocket",
#         "-f",
#         pdb_file
#     ]

#     try:
#         subprocess.run(
#             cmd,
#             check=True
#         )

#         print(f"[DONE] {protein}")

#     except subprocess.CalledProcessError:

#         print(f"[FAILED] {protein}")


# def main():

#     pdb_files = sorted(
#         glob.glob(
#             os.path.join(
#                 PDB_DIR,
#                 "*.pdb"
#             )
#         )
#     )

#     print(f"Total PDB files: {len(pdb_files)}")

#     for i, pdb in enumerate(pdb_files, start=1):

#         protein = os.path.basename(pdb)

#         print(f"\n[{i}/{len(pdb_files)}] {protein}")

#         run_fpocket(pdb)


# if __name__ == "__main__":
#     main()