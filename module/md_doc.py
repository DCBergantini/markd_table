import snakemd
import re
import unidecode
import pandas as pd
import pathlib
import argparse

class MarkTable:

    left=snakemd.generator.Table.Align.LEFT
    center=snakemd.generator.Table.Align.CENTER
    right=snakemd.generator.Table.Align.RIGHT

    MD_COLUMNS=["Column", "Type", "Example Value", "Description", "Format"]
    
    MD_ALIGN_LEFT=[left, left, left, left, left]
    MD_ALIGN_RIGHT=[right, right, right, right, right]
    MD_ALIGN_CENTER=[center, center, center, center, center]

    MD_ALIGN_LCENTER=[left, center, center, center, center]
    MD_ALIGN_RCENTER=[right, center, center, center, center]

    def generate_doc_md(name: str, dataframe, output: str, align_type: list):
        
        doc = snakemd.new_doc("README")

        doc.add_header(name)
        doc.add_paragraph("@DESCRIPTION@")
        
        doc.add_header("Model").demote()

        table_doc_md=[]

        for column in dataframe.columns:

            if dataframe[str(column)].dtype == "object":
                
                table_doc_md.append([unidecode.unidecode(column), dataframe[str(column)].dtype, unidecode.unidecode(dataframe[str(column)].values[0]), "@DESCRIPTION@", "@FORMAT@"])

            else: 
                table_doc_md.append([unidecode.unidecode(column), dataframe[str(column)].dtype, dataframe[str(column)].values[0], "@DESCRIPTION@", "@FORMAT@"])

        doc.add_table(
        MarkTable.MD_COLUMNS,
        table_doc_md,
        align_type
        )

        return doc.output_page(dump_dir=f"{output}\\{name}.md")


__name__ = "__main__"