def add_recursive(arr):
    '''
    Get sum of an array in a recursive manner
    Base case : Array is empty or is of size 1
    '''
    if (len(arr) == 0):
        return 0
    elif (len(arr) == 1):
        return arr[0]
    else:
        arr_len = len(arr)
        return arr[0] + add_recursive(arr[1:arr_len])



if __name__ == "__main__":
    test_arr = [1,2,3,4]
    print(add_recursive(test_arr))

