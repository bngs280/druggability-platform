import os
import subprocess

def run_fpocket(pdb_file):

    cmd = ["fpocket", "-f", pdb_file]

    subprocess.run(cmd, check=True)

    # fpocket output folder
    out_dir = pdb_file.replace(".pdb", "") + "_out"

    info_file = os.path.join(out_dir, os.path.basename(pdb_file).replace(".pdb", "_info.txt"))

    return info_file
