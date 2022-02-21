import re
from statistics import mode

class VerifyType():

    def __check_date_value(value):
                
        if re.fullmatch(r"([0-9]{,2}\/[0-9]{,2}\/[0-9]{4,})", value):

            return "date"

        elif re.fullmatch(r"([0-9]{,2}\-[0-9]{,2}\-[0-9]{4,})", value):

            return "date"

        elif re.fullmatch(r"([0-9]{,2}\.[0-9]{,2}\.[0-9]{4,})", value):
            
            return "date"

        elif re.fullmatch(r"([0-9]{4,}\/[0-9]{,2}\/[0-9]{,2})", value):
            
            return "date"

        elif re.fullmatch(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2})", value):
            
            return "date"

        elif re.fullmatch(r"([0-9]{4,}\.[0-9]{,2}\.[0-9]{,2})", value):
            
            return "date"
        
        else: 
            
            return False 
    

    def configurated_type(list_values: list):
        
        list_types=[]
        
        list_values = [value for value in list_values if value]

        for value in list_values:

            if (isinstance(value, str)==True):

                if re.fullmatch(r"^[0]\d*", value):
                    
                    list_types.append("string_number")
                
                elif re.fullmatch(r"^[1-9]\d*", value):
                    
                    list_types.append("number_integer")

                elif re.fullmatch(r"^[+-]?(\d+([\.\,])?)*", value):
                    
                    list_types.append("number_decimal")
    
                elif VerifyType.__check_date_value(value)=="date":
                
                    list_types.append("date")
                
                elif re.fullmatch(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2}\ [0-9]{,2}\:[0-9]{,2}\:[0-9]{,2}\.?[0-9]*)", value):
                    
                    list_types.append("datetime")
                
                elif not value:
                    list_types.append("undefined")
        
        if len(list_types) == 0:
            list_types.append("None")

        return mode(list_types)


    def type_SQL(list_values: list):
        
        
        list_types=[]
        list_len=[]
        list_values = [value for value in list_values if value]

        for value in list_values:

            if (isinstance(value, str)==True):

                if re.fullmatch(r"^[0]\d*", value):
                    
                    list_types.append("int")
                
                elif re.fullmatch(r"^[1-9]\d*", value):
                    
                    list_types.append("int")

                elif re.fullmatch(r"^[+-]?(\d+([\.\,])?)*", value):
                    
                    list_types.append("decimal")
    
                elif VerifyType.__check_date_value(value)=="date":
                
                    list_types.append("date")
                
                elif re.fullmatch(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2}\ [0-9]{,2}\:[0-9]{,2}\:[0-9]{,2}\.?[0-9]*)", value):
                    
                    list_types.append("datetime")

                else:
                    tamanho = len(value)
                    list_len.append(tamanho)
                    list_types.append(f"Varchar()")

        if len(list_types) == 0:
            list_types.append("None")
                
        if mode(list_types) == "Varchar()":
           type = f"Varchar({str(max(list_len)*2)})"
        
        else:
            type = mode(list_types)

        return type


    def python_type(list_values: list):
        
        list_types=[]
        list_values = [value for value in list_values if value]

        for value in list_values:

            if (isinstance(value, str)==True):

                if re.fullmatch(r"^[0]\d*", value):
                    
                    list_types.append("int")
                
                elif re.fullmatch(r"^[1-9]\d*", value):
                    
                    list_types.append("int")

                elif re.fullmatch(r"^[+-]?(\d+([\.\,])?)*", value):
                    
                    list_types.append("float")
    
                elif VerifyType.__check_date_value(value)=="date":
                
                    list_types.append("date")
                
                elif re.fullmatch(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2}\ [0-9]{,2}\:[0-9]{,2}\:[0-9]{,2}\.?[0-9]*)", value):
                    
                    list_types.append("datetime")
                
                elif not value:
                    list_types.append("None")
        
                else:
                    list_types.append("str")
        
        if len(list_types) == 0:
            list_types.append("None")

        return mode(list_types)


__name__=="__main__"