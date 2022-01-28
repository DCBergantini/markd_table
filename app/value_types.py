import re
from statistics import mode

class VerifyType():

    def __check_date_value(value):
                
        if re.match(r"([0-9]{,2}\/[0-9]{,2}\/[0-9]{4,})", value):

            return "date"

        elif re.match(r"([0-9]{,2}\-[0-9]{,2}\-[0-9]{4,})", value):

            return "date"

        elif re.match(r"([0-9]{,2}\.[0-9]{,2}\.[0-9]{4,})", value):
            
            return "date"

        elif re.match(r"([0-9]{4,}\/[0-9]{,2}\/[0-9]{,2})", value):
            
            return "date"

        elif re.match(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2})", value):
            
            return "date"

        elif re.match(r"([0-9]{4,}\.[0-9]{,2}\.[0-9]{,2})", value):
            
            return "date"
        
        else: 
            
            return False 
    

    def configurated_type(list_values: list):
        
        list_types=[]
        

        for value in list_values:

            if (isinstance(value, str)==True):

                if re.match(r"^[0]\d*", value):
                    
                    list_types.append("string_number")
                
                elif re.match(r"[1-9]*", value):
                    
                    list_types.append("number_integer")

                elif re.match(r"(\d*[\,\.])*\d*", value):
                    
                    list_types.append("number_decimal")
    
                elif VerifyType.__check_date_value(value)=="date":
                
                    list_types.append("date")
                
                elif re.match(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2}\ [0-9]{,2}\:[0-9]{,2}\:[0-9]{,2}\.?[0-9]*)", value):
                    
                    list_types.append("datetime")

        return mode(list_types)


    def type_SQL(list_values: list):
        
        
        list_types=[]
        list_len=[]

        for value in list_values:

            if (isinstance(value, str)==True):

                if re.match(r"^[0]\d*", value):
                    
                    list_types.append("int")
                
                elif re.match(r"[1-9]*", value):
                    
                    list_types.append("int")

                elif re.match(r"(\d*[\,\.])*\d*", value):
                    
                    list_types.append("decimal")
    
                elif VerifyType.__check_date_value(value)=="date":
                
                    list_types.append("date")
                
                elif re.match(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2}\ [0-9]{,2}\:[0-9]{,2}\:[0-9]{,2}\.?[0-9]*)", value):
                    
                    list_types.append("datetime")
                
                else:
                    tamanho = len(value)
                    list_len.append(tamanho)
                    list_types.append(f"Varchar()")
        
        if mode(list_types) == "Varchar()":
           type = f"Varchar({str(max(list_len)*2)})"
        
        else:
            type = mode(list_types)

        return type


    def python_type(list_values: list):
        
        list_types=[]

        for value in list_values:

            if (isinstance(value, str)==True):

                if re.match(r"^[0]\d*", value):
                    
                    list_types.append("int")
                
                elif re.match(r"[1-9]*", value):
                    
                    list_types.append("int")

                elif re.match(r"(\d*[\,\.])*\d*", value):
                    
                    list_types.append("float")
    
                elif VerifyType.__check_date_value(value)=="date":
                
                    list_types.append("date")
                
                elif re.match(r"([0-9]{4,}\-[0-9]{,2}\-[0-9]{,2}\ [0-9]{,2}\:[0-9]{,2}\:[0-9]{,2}\.?[0-9]*)", value):
                    
                    list_types.append("datetime")
                
                else:
                    list_types.append("str")

        return mode(list_types)


__name__=="__main__"