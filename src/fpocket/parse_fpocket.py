import os
import re


def parse(info_file):
    pockets = []
    pocket = None

    with open(info_file) as f:
        for line in f:
            line = line.strip()

            if line.startswith("Pocket"):
                if pocket:
                    pockets.append(pocket)
                pocket = {"Pocket": line}

            m = re.search(r"Score\s*:\s*([0-9.]+)", line)
            if m and pocket is not None:
                pocket["Score"] = float(m.group(1))

            m = re.search(r"Druggability Score\s*:\s*([0-9.]+)", line)
            if m and pocket is not None:
                pocket["Druggability"] = float(m.group(1))

            m = re.search(r"Total SASA\s*:\s*([0-9.]+)", line)
            if m and pocket is not None:
                pocket["SASA"] = float(m.group(1))

        if pocket:
            pockets.append(pocket)

    return pockets


def parse_all(base_dir):
    all_results = []

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith("_info.txt"):
                file_path = os.path.join(root, file)

                protein = file.replace("_info.txt", "")
                pockets = parse(file_path)

                for p in pockets:
                    p["Protein"] = protein
                    p["File"] = file_path
                    all_results.append(p)

    return all_results


if __name__ == "__main__":
    base_dir = "data/pdb"

    results = parse_all(base_dir)

    print(f"Total pockets parsed: {len(results)}")
    for r in results[:5]:
        print(r)

# import os
# import re


# def parse(info_file):

#     pockets=[]

#     pocket=None

#     with open(info_file) as f:

#         for line in f:

#             line=line.strip()

#             if line.startswith("Pocket"):

#                 if pocket:

#                     pockets.append(pocket)

#                 pocket={}

#                 pocket["Pocket"]=line

#             m=re.search(
#                 r"Score\s*:\s*([0-9.]+)",
#                 line
#             )

#             if m and pocket is not None:

#                 pocket["Score"]=float(
#                     m.group(1)
#                 )

#             m=re.search(
#                 r"Druggability Score\s*:\s*([0-9.]+)",
#                 line
#             )

#             if m and pocket is not None:

#                 pocket["Druggability"]=float(
#                     m.group(1)
#                 )

#             m=re.search(
#                 r"Total SASA\s*:\s*([0-9.]+)",
#                 line
#             )

#             if m and pocket is not None:

#                 pocket["SASA"]=float(
#                     m.group(1)
#                 )

#         if pocket:

#             pockets.append(pocket)

#     return pockets


# if __name__=="__main__":

#     file="data/pdb/P68871_out/P68871_info.txt"

#     result=parse(file)

#     print(result)