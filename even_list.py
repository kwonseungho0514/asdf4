from typing import List

def even_list(int_list: List[int]) -> List[int]:
    result = []

    for element in int_list:
        if(element % 2 == 0):
            result.append(element)

    return result