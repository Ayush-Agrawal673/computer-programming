# write a python function to sort an arraay of integars ina ascending order 
def merge_sort(arr):
    # Base case: if the array has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array
    mid = len(arr) // 2
    
    # Split the array into two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge the two sorted lists into a sorted result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements in the left or right half
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr) 