def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    new_list=[]
    for fruit in fruits:
        
        if fruit!='apple':
            new_list.append(fruit)
        
    return new_list

