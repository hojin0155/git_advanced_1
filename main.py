from typing import List
# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    result = []
    for num in int_list:
        if num % 2 == 0:
            result.append(num)
    return result

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    result = 0
    for num in even_int_list:
            result = result + num*num
    return result

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
    
# Boilerplate code
if __name__ == "__main__":
    main()