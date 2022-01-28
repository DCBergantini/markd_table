from app import args
from app import read_files
from app import md_construct
import os

def main():
    
    args_passed = args.get_args()
    valid_args = args.verify(args_passed)
      
    if args_passed.directory:
        
        directory=[csv for csv in os.listdir(args_passed.directory) if ".csv" in csv]
        
        for file in directory:
            
            path=f"{args_passed.directory}/{file}"
            matrix = read_files.csv(path, delimiter="\t")
            dataset = read_files.Dataset.matrix_to_dataset(matrix=matrix, skiprows=0)
            
            schema = md_construct.generate_schema_table(dataset, choosed_type=args_passed.type_format)                
            variants = [md_construct.identify_variants(column) for column in dataset]
            nulls = [column.column_name for column in dataset if md_construct.identify_null_columns(column) is True]

            documentation = md_construct.generate_markdown(file, dataset, schema, variants, nulls)
            
            md_construct.generate_markdown_file(documentation, args_passed.output_dir)

    elif args_passed.file:
        
        if ".csv" in args_passed.file:
            
            matrix = read_files.csv(args_passed.file, delimiter="\t")
            dataset = read_files.Dataset.matrix_to_dataset(matrix=matrix, skiprows=0)
            
            schema = md_construct.generate_schema_table(dataset, choosed_type=args_passed.type_format)                
            variants = [md_construct.identify_variants(column) for column in dataset]

            nulls = [column.column_name for column in dataset if (md_construct.identify_null_columns(column) is True)]
            documentation = md_construct.generate_markdown(os.path.basename(args_passed.file), dataset, schema, variants, nulls)
            
            #md_construct.generate_markdown_file(documentation, args_passed.output_dir)        
        
        else:
            
            raise Exception("\n\nOnly accept [.csv] format files.")



        


if __name__=='__main__':

    main()