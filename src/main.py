import argparse
import sys
from generator import MarkTable
from reader import read_file

parser = argparse.ArgumentParser(description="Generate a structured markdown documentation template for a tabular file.")
parser.add_argument("-s", "--source_file", type=str, help="The tabular file you want to generate the documentation template for.")
parser.add_argument("-o", "--output_dir", type=str, help="The directory to write the generated markdown file.")
parser.add_argument("-H", "--header", action="store_true")
parser.add_argument("-d", "--delimiter", action="store_true")

def init(args):

    file_name, dataframe = read_file(
        path=args.source_file,
        delimiter=args.delimiter,
        header=args.header
    )

    doc = MarkTable.generate(name=file_name, dataframe=dataframe)

    if args.output_dir:
        doc.output_page(args.output_dir)
    else:
        print(doc)

if __name__=='__main__':
    args = parser.parse_args()

    if args.source_file is None:
        parser.print_help(sys.stderr)
        sys.exit()

    init(args)
