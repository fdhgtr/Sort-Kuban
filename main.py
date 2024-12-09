import random

# Původní pole
array = [34, 7, 23, 32, 5, 62, 32, 9, 54, 18]
print("Původní pole:", array)

# Funkce pro Bubble Sort 
def bubble_sort(array):
    
    for i in range(len(array)):
        
        for j in range(len(array) - i - 1):
            
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 
    return array

# Seřazení pole pomocí Bubble Sort
sorted_array = bubble_sort(array)
print("Bubble sort:", sorted_array)

# Funkce pro Bogo Sort 
def bogo_sort(array):
    
    def is_sorted(array):
        return array == sorted(array)  
    
    
    while not is_sorted(array):
        random.shuffle(array)  
    return array

# Seřazení pole pomocí Bogo Sort
sorted_array2 = bogo_sort(array.copy())
print("Bogo Sort:", sorted_array2)

# Funkce pro Selection Sort 
def selection_sort(array):
    
    for m in range(len(array)):
        

        o = m
        
        for k in range(m + 1, len(array)):
            
            if array[k] < array[o]:
                o = k
        
        
        array[m], array[o] = array[o], array[m]
    return array

# Seřazení pole pomocí Selection Sort
sorted_array3 = selection_sort(array.copy())
print("Selection Sort:", sorted_array3)

# Funkce pro Insertion Sort 
def insertion_sort(array):
    
    for q in range(1, len(array)):
        
        lol = array[q]
        
        n = q - 1
        
        
        while n >= 0 and array[n] > lol:
            array[n + 1] = array[n]
            n -= 1
        
        
        array[n + 1] = lol
    
    return array

# Seřazení pole pomocí Insertion Sort
sorted_array4 = insertion_sort(array.copy())
print("Insertion Sort:", sorted_array4)