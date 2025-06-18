import numpy as np

def calculate(list):
    if len(list) != 9:                                          # Error when list contains more/less than 9 numbers
        raise ValueError("List must contain nine numbers.")     #

    matrix_list = np.array(list).reshape(3,3)  # Change list to 3x3 matrix

    max_row = matrix_list.max(axis=0)       #
    max_col = matrix_list.max(axis=1)       # Calculate max
    max_flat = matrix_list.max()            #

    min_row = matrix_list.min(axis=0)       #
    min_col = matrix_list.min(axis=1)       # Calculate min
    min_flat = matrix_list.min()            #

    sum_row = matrix_list.sum(axis=0)       #
    sum_col = matrix_list.sum(axis=1)       # Calculate sum
    sum_flat = matrix_list.sum()            #

    std_row = matrix_list.std(axis=0)       #
    std_col = matrix_list.std(axis=1)       # Calculate standard deviation
    std_flat = matrix_list.std()            #

    var_row = matrix_list.var(axis=0)       #
    var_col = matrix_list.var(axis=1)       # Calculate variance
    var_flat = matrix_list.var()            #

    mean_row = matrix_list.mean(axis=0)       #
    mean_col = matrix_list.mean(axis=1)       # Calculate mean
    mean_flat = matrix_list.mean()            #



    calculations =  {
        "max": [max_row.tolist(), max_col.tolist(), max_flat.item()],           #
        "min": [min_row.tolist(), min_col.tolist(), min_flat.item()],           #
        "sum": [sum_row.tolist(), sum_col.tolist(), sum_flat.item()],           # Return with tolist() and item() to change the results from arrays to python lists and from a scalar to float
        "std": [std_row.tolist(), std_col.tolist(), std_flat.item()],           #
        "var": [var_row.tolist(), var_col.tolist(), var_flat.item()],           #
        "mean": [mean_row.tolist(), mean_col.tolist(), mean_flat.item()]        #
    }

    return calculations
