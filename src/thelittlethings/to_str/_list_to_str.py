def list_to_str(list, final_sep="and", empty_str="None"):
    if len(list) == 0:
        return empty_str
        
    string = list[-1]

    if len(list) > 1:
        string = f"{list[-2]} {final_sep} {string}"
    
    for i in range(3, len(list) + 1):
        string = f"{list[-i]}, {string}"
    
    return string