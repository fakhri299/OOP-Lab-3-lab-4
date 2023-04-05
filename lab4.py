def print_smaller_elements(arr, x):
    
    for element in arr:
        if element < x:
            print(element)


arr =[5, 15, 25, 35, 45]
x = 30
print_smaller_elements(arr, x)