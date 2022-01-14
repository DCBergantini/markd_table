import snakemd
import re
import unidecode
import pandas as pd
import pathlib
import argparse
from module import md_doc
from module import read_file

parser = argparse.ArgumentParser(description="Generate .md tables documentation from a tabular file.")
parser.add_argument("--dir_source_files", type=str, help="Insert the directory where exist the file or files, with tabular format that you want to transform in markdown documentation.")
parser.add_argument("--dir_output", type=str, help="Insert the directory where you want to create the .md file ou files.")
parser.add_argument("--table_format", type=str, help="Choose a format: Center, Left, Right, f_left, f_right")

parser.add_argument("-H", "--Header", action="store_true")
parser.add_argument("-S", "--csv_splitter", action="store_true")

args = parser.parse_args()

if __name__=='__main__':

    name, dataframe=read_file.read_file(args.dir_source_files, csv_splitter=args.csv_splitter, header=args.header)

    if args.table_format.lower()=="left":

        md_doc.MarkTable.generate_doc_md(name, dataframe, args.dir_output, md_doc.MarkTable.MD_ALIGN_LEFT)

        print(f".md files were generated in {args.dir_output}")

    elif args.table_format.lower()=="center":

        md_doc.MarkTable.generate_doc_md(name, dataframe, args.dir_output, md_doc.MarkTable.MD_ALIGN_CENTER)

        print(f".md files were generated in {args.dir_output}")


    elif args.table_format.lower()=="right":

        md_doc.MarkTable.generate_doc_md(name, dataframe, args.dir_output, md_doc.MarkTable.MD_ALIGN_RIGHT)

        print(f".md files were generated in {args.dir_output}")


    elif args.table_format.lower()=="f_left":

        md_doc.MarkTable.generate_doc_md(name, dataframe, args.dir_output, md_doc.MarkTable.MD_ALIGN_LCENTER)

        print(f".md files were generated in {args.dir_output}")


    elif args.table_format.lower()=="f_right":

        md_doc.MarkTable.generate_doc_md(name, dataframe, args.dir_output, md_doc.MarkTable.MD_ALIGN_RCENTER)

        print(f".md files were generated in {args.dir_output}")
