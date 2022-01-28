import argparse
import sys
def get_args():

    parser = argparse.ArgumentParser(description="Generate a structured markdown documentation template for a tabular file;")


    parser.add_argument("-O", "--output_dir", type=str, required=True, help="The directory to write the generated markdown file;")
    parser.add_argument("--header", type=int, help="Number of lines to skip to the header;")
    parser.add_argument("--delimiter", type=str, help="CSV Delimiter pattern to use;")
    parser.add_argument("--type_format", type=str, choices=['sql', 'markd_config', 'python_language'], help="Please, choose a type format.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-D", "--directory", type=str, help="The tabular file you want to generate the documentation template for, needs to  be provided a full path;")
    group.add_argument("-F", "--file", type=str, help="The tabular file you want to generate the documentation template for, needs to  be provided a full path with /file.csv;")

    return parser.parse_args()


def verify(args):

    if args.output_dir is None:
        
        sys.exit()
        

    if (args.directory is None) and (args.file is None):
        
        sys.exit()
    
    if args.header is None:
        
        return True 

    if args.delimiter is None:
        
        return True 

__name__=="__main__"