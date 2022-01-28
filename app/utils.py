

def get_unique_values(list: list):
    
    unique_list=[]

    for item in list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list
    


__name__=="__main__"