import os
import re


def parse(info_file):

    pockets=[]

    pocket=None

    with open(info_file) as f:

        for line in f:

            line=line.strip()

            if line.startswith("Pocket"):

                if pocket:

                    pockets.append(pocket)

                pocket={}

                pocket["Pocket"]=line

            m=re.search(
                r"Score\s*:\s*([0-9.]+)",
                line
            )

            if m and pocket is not None:

                pocket["Score"]=float(
                    m.group(1)
                )

            m=re.search(
                r"Druggability Score\s*:\s*([0-9.]+)",
                line
            )

            if m and pocket is not None:

                pocket["Druggability"]=float(
                    m.group(1)
                )

            m=re.search(
                r"Total SASA\s*:\s*([0-9.]+)",
                line
            )

            if m and pocket is not None:

                pocket["SASA"]=float(
                    m.group(1)
                )

        if pocket:

            pockets.append(pocket)

    return pockets


if __name__=="__main__":

    file="data/pdb/P68871_out/P68871_info.txt"

    result=parse(file)

    print(result)