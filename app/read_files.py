
from dataclasses import dataclass

@dataclass(order=True)
class Dataset:
    
    column_name = ""
    column_values = []

    def matrix_to_dataset(matrix, skiprows):

        number_of_columns = len(matrix[skiprows])
        columns_names = matrix[skiprows]
        
        list_of_columns_info = []
        
        for column_index in range(0, number_of_columns):

            column=Dataset()
            column.column_name=columns_names[column_index]
            column.column_values=[i[column_index] for i in matrix[(skiprows+1):]]

            list_of_columns_info.append(column)
        
        return list_of_columns_info


def csv(path="C:/Users/bergantinid.APEXPARTNERS/Desktop/projects/markd_table/examples/demo.csv", delimiter="\t"):

    file = open(path, "r")
    
    list_rows = []

    for line in file:
        
        line = line.strip()
        line = line.split(delimiter)
        line = [item.replace('"', '') for item in line]

        list_rows.append(line)

    file.close()

    return list_rows

# teste = Dataset.matrix_to_dataset(csv(), 0)

# null_list = teste[6].column_values

# print(null_list)
# print(null_list)

__name__=="__main__"