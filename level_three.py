def find_Max_In_List(numbers):
    if not numbers:
        return ("Not happening")
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum
numbers= [100,9,84,345,433,45]
print (find_Max_In_List(numbers))