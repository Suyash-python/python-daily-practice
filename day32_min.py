def find_min(numbers):
    smallest = numbers[0]

    for num in numbers:
      if num < smallest:
        smallest = num
    
    return smallest

print(find_min([10,5,8,2,15]))
