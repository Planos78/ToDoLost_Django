arr = [1, 2, 1, 3, 5, 6, 4]
print("Array: ", arr)
Max_value = None
for x in arr:
    if Max_value is None or x > Max_value:
        Max_value = x
print('Max value in Array is', Max_value)
