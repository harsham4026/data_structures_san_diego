#python3


#funtion to sort the array

def get_max_n_numbers(input_array):
    # largest_num = 0
    # second_largest_num = 0
    # sorted_array = sorted(input_array)
    # array_length = len(sorted_array)
    # return sorted_array[array_length-1]*sorted_array[array_length-2]


    array_length = len(input_array)
    max_product = 0
    for x in range(array_length):
        for y in range(x+1,array_length):
            max_product= max(max_product,input_array[x]*input_array[y])
    return max_product




if __name__=='__main__':
    input_n = int(input())
    input =[int(x) for x in input().split()]
    print(input)
    print(get_max_n_numbers(input))
