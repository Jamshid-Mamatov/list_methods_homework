def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    count=fruits.count('apple')
    list_index=[]
    for index,fruit in enumerate(fruits):
        if fruit=='apple':
            fruits.remove('apple')
            list_index.append(index)

    return list_index