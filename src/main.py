import argparse
import sys
import pandas as pd
import os
import pathlib
import snakemd

def parser_reader():

    parser = argparse.ArgumentParser(description="Generate a structured markdown documentation template for a tabular file.")
    parser.add_argument("-S", "--source_file", type=str, help="The tabular file you want to generate the documentation template for.")
    parser.add_argument("-O", "--output_dir", type=str, help="The directory to write the generated markdown file.")
    parser.add_argument("--header", type=int, help="Number of lines to skip to the header.")
    parser.add_argument("--delimiter", type=str, help="CSV Delimiter pattern to use.")

    return parser.parse_args()


def read_file(path, delimiter: str = ";", header: int = 0, encoding: str = "utf8"):

    SUPPORTED_FORMATS = [".csv"]

    file_name=os.path.basename(path).split(".")[0]
    file_extension = pathlib.Path(path).suffix

    if file_extension not in SUPPORTED_FORMATS:
        raise Exception("""Unsupported file type.
                           Supported file types: csv""")


    dataframe = pd.read_csv(path, sep=delimiter, header=header, encoding=encoding)

    return file_name, dataframe


def identify_type(value):

    if ((isinstance(value, int)==True) or (isinstance(value, float)==True)):

        return "Number"
    
    elif (isinstance(value, str)==True):

        try:
            value=value.replace(",", ".")

            value=float(value)

            return "Number"
        
        except:
            
            return "String"

    elif (isinstance(value, bool)==True):

        return "Boolean"


def generate_schema(dataframe):

    for column in dataframe.columns:  
                        
        dataframe[f'{column}-Type']=dataframe[column].apply(lambda x: identify_type(x))
        
    return dataframe


def generate_schema_table(dataframe):

    table_schema=[]
    
    for column in dataframe.columns:
        
        if "-Type" not in str(column): 
            value=str(dataframe[column].mode(dropna=True).values[0])
            Type=str(dataframe[f'{column}-Type'].mode(dropna=True).values[0])

            table_schema.append([column, Type, value, "DESCRIPTION", "FORMAT"])


    return table_schema


def generate_variants(dataframe):
    
    lista_variants=[]
    
    for column in dataframe.columns:
         
        values=list(dataframe[column].astype(str).unique())
        
        variants={"column": str(column),
                "unique_values": values,
                "amount_finded":str(len(values))}

        lista_variants.append(variants)

    return lista_variants



def generate_nulls_columns(dataframe):
        
    null_columns=[]

    for column in dataframe.columns:
         
        if dataframe[column].isnull().all():
           
           null_columns.append(column)
        
    if not null_columns:
        
        null_columns.append("Todas colunas possuem valores!")

    
    return null_columns



def generate_variants_mais10(variants):
    
    variantes_info=[]

    for variant in variants:
        
        column=variant["column"]

        if (int(variant["amount_finded"]) > 10) and ("-Type" not in column):
            
            total_finded=int(variant["amount_finded"])
  
            value=variant["unique_values"][:10]
            total_finds=(total_finded-10)
            value.append(f"+{str(total_finds)}")

            variantes_info.append({"column_name": column, "list_values": value})

    return variantes_info           
           

def generate_variants_menos10(variants):

    variantes_info=[]

    for variant in variants:
        
        column=variant["column"]
        
        if (int(variant["amount_finded"]) < 10) and (int(variant["amount_finded"]) > 1) and ("-Type" not in column):
                
            dados=variant["unique_values"]

            variantes_info.append({"column_name": column, "list_values": dados})
                                                    
    return variantes_info


def generate_markdown(name, variant_mais10, variant_menos10, nulls_text, schema_table):

        COLUMNS = ["Column", "Type", "Example Value", "Description", "Format"]
        LEFT = snakemd.generator.Table.Align.LEFT
        LEFT_ALIGN = [LEFT, LEFT, LEFT, LEFT, LEFT]

        file_name = "_".join(name.lower().split(" "))

        doc = snakemd.new_doc(file_name)
        
        doc.add_header(name.title())
        doc.add_paragraph("DESCRIPTION")
        
        doc.add_header("Modelo").demote()
        doc.add_table(COLUMNS, schema_table, LEFT_ALIGN)

        doc.add_header("Dicionário").demote()

        for variant in variant_mais10:

            column_name=str(variant["column_name"])
            doc.add_paragraph(f"Foram observadas as seguintes variantes para a chave: {column_name}")
            doc.add_unordered_list(variant["list_values"])
            
        for variant in variant_menos10:
            
            column_name=str(variant["column_name"])
            doc.add_paragraph(f"Foram observadas as seguintes variantes para a chave: {column_name}")
            doc.add_unordered_list(variant["list_values"])

        doc.add_header("Colunas vazias").demote()
        
        doc.add_paragraph(f"Foram observadas as seguintes colunas sem valores:")
        doc.add_unordered_list(nulls_text)        
        
        return doc


def generate_markdown_file(documento, output_dir):

        documento.output_page(output_dir)
        
        return print(f"Documento criado com successo, no diretório: {output_dir}")



def init(args):


    for file in os.listdir(args.source_file):
        print(file)
        if file.endswith(".csv"):
            
            file_name, dataframe = read_file(
                path=f"{args.source_file}/{file}",
                delimiter=args.delimiter,
                header=args.header
            )
            text_variants_mais10=generate_variants_mais10(generate_variants(generate_schema(dataframe)))    
            text_variants_menos_10=generate_variants_menos10(generate_variants(generate_schema(dataframe)))

            text_nulls=generate_nulls_columns(dataframe)
            md_table=generate_schema_table(generate_schema(dataframe))

            md_document=generate_markdown(file_name, text_variants_mais10, text_variants_menos_10, text_nulls, md_table)

            generate_markdown_file(md_document, args.output_dir)

if __name__=='__main__':

    args=parser_reader()
    if args.source_file is None:
        args.print_help(sys.stderr)
        sys.exit()

    init(args)
