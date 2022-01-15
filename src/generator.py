import argparse
import pandas as pd
import snakemd
from unidecode import unidecode

class MarkTable:

    def generate(name: str, dataframe):

        COLUMNS = ["Column", "Type", "Example Value", "Description", "Format"]
        LEFT = snakemd.generator.Table.Align.LEFT
        LEFT_ALIGN = [LEFT, LEFT, LEFT, LEFT, LEFT]

        file_name = "_".join(name.lower().split())

        doc = snakemd.new_doc(file_name)
        doc.add_header(name.title())
        doc.add_paragraph("DESCRIPTION")
        doc.add_header("Model").demote()

        table = []

        for column in dataframe.columns:
            col_name = column
            col_first_value = dataframe[col_name].values[0]
            table.append([
                col_name,
                "TYPE",
                col_first_value,
                "DESCRIPTION",
                "FORMAT"]
            )

        doc.add_table(COLUMNS, table, LEFT_ALIGN)

        return doc

__name__ = "__main__"
