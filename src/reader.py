import pandas as pd
import pathlib
import os

def read_file(path, delimiter: str, header: int):

    SUPPORTED_FORMATS = [".txt", ".csv", ".xls", ".xlsx"]

    file_name=os.path.basename(path).split(".")[0]
    file_extension = pathlib.Path(path).suffix
    delimiter = delimiter or ","
    header = header or 0

    if file_extension not in SUPPORTED_FORMATS:
        raise Exception("""Unsupported file type.
                           Supported file types: txt, csv, xls, xlsx""")

    if file_extension in [".csv", ".txt"]:
        dataframe = pd.read_csv(path, sep=delimiter, header=header)
    if file_extension in [".xls", ".xlsx"]:
        dataframe = pd.read_excel(path, header=header)

    return file_name, dataframe

__name__=="__main__"
