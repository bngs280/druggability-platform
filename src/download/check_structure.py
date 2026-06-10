import os


def exists(uniprot):

    path = f"data/pdb/{uniprot}.pdb"

    return os.path.exists(path)


if __name__ == "__main__":

    print(exists("P68871"))