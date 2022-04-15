def list(list, final_sep="and", empty_str="nothing"):
    """
    convert a list to a string with a final separator
    """

    if len(list) == 0:
        return empty_str
        
    string = str(list[-1])

    if len(list) > 1:
        string = f"{str(list[-2])} {final_sep} {string}"
    
    for i in range(3, len(list) + 1):
        string = f"{str(list[-i])}, {string}"
    
    return string