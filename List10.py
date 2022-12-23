def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    count_0=0
    count_1=0
    for item in list1:
        if item==0:
            count_0+=1
        else:
            count_1+=1

    return [count_1,count_0]
