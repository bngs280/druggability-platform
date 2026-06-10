import hashlib
import os

PDB_DIR = "data/pdb"

def get_sequence_hash(sequence):

    return hashlib.md5(
        sequence.encode()
    ).hexdigest()

def structure_exists(sequence):

    seq_hash = get_sequence_hash(sequence)

    pdb_file = f"{PDB_DIR}/{seq_hash}.pdb"

    return os.path.exists(pdb_file), pdb_file