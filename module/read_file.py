
import pathlib
import pandas as pd
import os

def read_file(source_file, csv_splitter: str, header: int):

    if csv_splitter is None: 
        csv_splitter = ","
    
    if header is None:
        header=0

    file_extension = pathlib.Path(source_file).suffix

    if file_extension==".csv" or file_extension==".txt":
        
        file=pd.read_csv(source_file, sep=csv_splitter, header=header)
    
    elif file_extension==".xlsx" or file_extension==".xls":
        
        file=pd.read_excel(source_file, header=header)
    
    else:
        raise Exception("""Type of file not suported by the current Version!
                            Try: .xlsx, .csv, .xls or .txt(csv format)""")
    
    name_file=os.path.basename(source_file).split(".")[0]
    
    return name_file, file


__name__=="__main__"