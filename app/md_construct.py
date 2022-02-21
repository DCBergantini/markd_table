import snakemd
from app import value_types
from app import utils

def generate_schema_table(list_dataset, choosed_type):

    table_schema=[]
    
    for column in list_dataset:
        list_values = [value for value in column.column_values if value]
        
        if len(list_values) > 0:
            value = list_values[0]
        
        else:
            value = None
        
        if choosed_type=="sql":

            Type=value_types.VerifyType.type_SQL(column.column_values)
        
        elif choosed_type=="markd_config":

            Type=value_types.VerifyType.configurated_type(column.column_values)
        
        elif choosed_type=="python_language":
        
            Type=value_types.VerifyType.python_type(column.column_values)
        
        else:
            Type="undefinied"
        

        table_schema.append([column.column_name, Type, value, "DESCRIPTION", "FORMAT"])

    return table_schema

def identify_variants(dataset):

    column_name = dataset.column_name
    values=utils.get_unique_values(dataset.column_values)

    if values and len(values) > 10:
        
        list_variants=values[:10]
        total_finds=(len(utils.get_unique_values(dataset.column_values))-10)
        amount_finded=f"+{str(total_finds)}"

        variants_info= {"column_name": column_name,
                            "variants": list_variants, 
                            "amount_finded": amount_finded}
        
        return variants_info

    elif values and len(values) <= 10:
        
        list_variants=values

        variants_info= {"column_name": column_name,
                            "variants": list_variants}

        return variants_info
    
    else:
        pass

def identify_null_columns(dataset):

    values = utils.get_unique_values(dataset.column_values)
    print(values)
    if bool(values)==False:

        return True
    
    else:

        return False

def generate_markdown_file(documento, output_dir):

        documento.output_page(output_dir)
        
        return print(f"Documento criado com successo, no diretório: {output_dir}")

def generate_markdown(name, list_dataset, schema, variants, nulls):

        COLUMNS = ["Column", "Type", "Example Value", "Description", "Format"]
        LEFT = snakemd.generator.Table.Align.LEFT
        LEFT_ALIGN = [LEFT, LEFT, LEFT, LEFT, LEFT]

        file_name = "_".join(name.lower().split(" "))

        doc = snakemd.new_doc(file_name)
        
        doc.add_header(name.title())
        doc.add_paragraph("DESCRIPTION")
        
        doc.add_header("Modelo").demote()
        doc.add_table(COLUMNS, schema, LEFT_ALIGN)

        doc.add_header("Dicionário").demote()

        for variant in variants:

            column_name=str(variant["column_name"])
            doc.add_paragraph(f"Foram observadas as seguintes variantes para a chave: {column_name}")            
            doc.add_unordered_list(variant["variants"])

        doc.add_header("Colunas vazias").demote()
        doc.add_paragraph(f"Foram observadas as seguintes colunas sem valores:")       
        doc.add_unordered_list(nulls)        
                
        return doc


__name__=="__main__"