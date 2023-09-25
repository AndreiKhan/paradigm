def binary(arr, number):
    arr_start = 0
    arr_end = len(arr) - 1
    
    while arr_start <= arr_end:
        
        arr_center = (arr_start + arr_end) // 2
        search_number = arr[arr_center]
        
        if search_number == number:
            return arr_center
        
        if search_number > number:
            arr_end = arr_center - 1
        else:
            arr_start = arr_center + 1
    
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = 7

print(f'Индекс числа {number} в массиве = {binary(array, number)}')