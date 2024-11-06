from typing import List

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum = 0

    for element in even_int_list:
        sum = sum + element * element
    
    return sum